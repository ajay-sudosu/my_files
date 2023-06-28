import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
channel.exchange_declare(exchange='my_topic', exchange_type=ExchangeType.topic)
# queue = channel.queue_declare(queue='', exclusive=True)
# channel.queue_bind(exchange='my_topic', queue=queue.method.queue, routing_key='user.europe')
user_payment_msg = 'Hello world'
channel.basic_publish(exchange='my_topic', routing_key='user.payments.europe', body=user_payment_msg)
print(f'sent message: {user_payment_msg}')
connection.close()