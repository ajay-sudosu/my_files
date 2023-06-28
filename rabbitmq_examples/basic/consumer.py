import pika


def message_received_function(ch, method, properties, body):
    print(f"Received message: {body}")


connection_parameters = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
channel.queue_declare(queue="letterbox")
channel.basic_consume(queue="letterbox", auto_ack=True, on_message_callback=message_received_function)
print("start consuming")
channel.start_consuming()
