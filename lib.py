import jsons
import json
import pika
from munch import munchify
from status import Status


def callback(ch, method, props, body, func):
    print("Callback")
    try:
        request = munchify(json.loads(body))
        response_payload = func(request)
        response = {"payload": response_payload, "status": Status.SUCCESS}
    except Exception as e:
        response = {"payload": str(e), "status": Status.ERROR}
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=jsons.dumps(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)