import random
import time
import pika
from pika.exchange_type import ExchangeType


def message_received_function(ch, method, properties, body):
    print(f"consumer A received this message: {body}")


connection_parameters = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)
queue = channel.queue_declare(queue="", exclusive=True)  # exclusive tells RMQ to delete queue if connection is closed
channel.queue_bind(exchange='pubsub', queue=queue.method.queue)
channel.basic_consume(queue=queue.method.queue, on_message_callback=message_received_function)
print("start consuming")
channel.start_consuming()

