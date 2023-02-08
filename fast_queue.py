import pika
from objection_engine import get_all_music_available
from lib import callback

def func_executor(request):
    music = get_all_music_available()
    return {"musicCodes": music}

def callback_interceptor(ch, method, props, body):
    return callback(ch, method, props, body, func_executor)


connection = pika.BlockingConnection()
channel = connection.channel()

channel.queue_declare(queue='oe_fast')

channel.basic_consume(queue='oe_fast', on_message_callback=callback_interceptor)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.basic_qos(prefetch_count=1)
channel.start_consuming()
