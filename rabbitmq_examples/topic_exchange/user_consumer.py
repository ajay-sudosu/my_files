import pika
from pika.exchange_type import ExchangeType


def message_received_function(ch, method, properties, body):
    print(f"User consumer received this message: {body}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

connection_parameters = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
channel.exchange_declare(exchange='my_topic', exchange_type=ExchangeType.topic)
queue = channel.queue_declare(queue="", exclusive=True)  # exclusive tells RMQ to delete queue if connection is closed
channel.queue_bind(exchange='my_topic', queue=queue.method.queue, routing_key='*.payments.*')
channel.basic_consume(queue=queue.method.queue, on_message_callback=message_received_function)
print("start consuming")
channel.start_consuming()

