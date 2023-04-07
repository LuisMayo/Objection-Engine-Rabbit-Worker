import pika
from objection_engine.renderer import render_comment_list
from objection_engine.beans.comment import Comment
from lib import callback

def func_executor(request):
    comment_list = []
    for com in request.payload.comment_list:
        comment_list.append(Comment(**com))
    request.payload.comment_list = comment_list
    render_comment_list(**request.payload)
    return {"url": request.payload.output_filename}

def callback_interceptor(ch, method, props, body):
    return callback(ch, method, props, body, func_executor)

params = pika.ConnectionParameters(heartbeat=600,
                                       blocked_connection_timeout=300)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.basic_qos(prefetch_count=1)

channel.queue_declare(queue='oe_slow')

channel.basic_consume(queue='oe_slow', on_message_callback=callback_interceptor)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
