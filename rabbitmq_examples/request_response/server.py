import pika


def on_request_callback(ch, method, properties, body):

    print(f"Request received: {properties.correlation_id}")
    ch.basic_publish(exchange='', routing_key=properties.reply_to, body=f'Its your reply to : {properties.correlation_id}')


connection_channel = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_channel)
channel = connection.channel()

channel.queue_declare(queue='request_queue')
channel.basic_consume(queue='request_queue', auto_ack=True, on_message_callback=on_request_callback)

print("Starting server")
channel.start_consuming()


