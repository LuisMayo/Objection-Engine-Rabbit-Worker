import pika
# from objection_engine.v4.make_movie import render_comment_list
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


connection = pika.BlockingConnection()
channel = connection.channel()

channel.queue_declare(queue='oe_slow')

channel.basic_consume(queue='oe_slow', on_message_callback=callback_interceptor)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.basic_qos(prefetch_count=1)
channel.start_consuming()
