import time
import random
from celery_tasks.celery_config import celery_app


@celery_app.task(queue='add_blocks')
def add_back_blocks(block):
    try:
        start = time.time()
        time.sleep(10)
        end = time.time()
        return {"time_taken": end-start, "message": f"Block number- {block} has been added successfully."}
    except Exception as error:
        print(error)


