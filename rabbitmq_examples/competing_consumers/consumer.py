import random
import time

import pika


def message_received_function(ch, method, properties, body):
    processing_time = random.randint(1,6)
    print(f"This will take {processing_time} to complete the task: {body}.")
    time.sleep(processing_time)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("Processing finished")


connection_parameters = pika.ConnectionParameters("localhost")
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
channel.queue_declare(queue="letterbox")
channel.basic_qos(prefetch_count=1) # tells rabbitmq do not send more than one message to a consumer when a task is already under progress
channel.basic_consume(queue="letterbox", on_message_callback=message_received_function)
print("start consuming")
channel.start_consuming()
