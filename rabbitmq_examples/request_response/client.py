import pika
import uuid


def on_reply_callback(ch, method, properties, body):
    print(f"reply received {body}")


connection_channel = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_channel)
channel = connection.channel()

reply_queue = channel.queue_declare(queue='')
# reply_queue = channel.queue_declare(queue='request_queue') (both the options are correct , we can send reply to
# the same queue where we are sending the request)
channel.basic_consume(queue=reply_queue.method.queue, auto_ack=True, on_message_callback=on_reply_callback)

channel.queue_declare(queue='request_queue')
message = 'Can I request a reply?'
cor_id = str(uuid.uuid4())
print(f'sending request for : {cor_id}')
channel.basic_publish(exchange='', routing_key='request_queue',
                      properties=pika.BasicProperties(reply_to=reply_queue.method.queue, correlation_id=cor_id),
                      body=message)
print("Starting client")
channel.start_consuming()


