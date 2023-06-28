from fastapi import FastAPI
from celery_tasks.machine_tasks import add_back_machines
from celery_tasks.block_tasks import add_back_blocks
fast_app = FastAPI()


@fast_app.post("/add-machines")
def add_machines():
    try:
        for machine in range(10):
            add_back_machines.delay(machine)
        return {"message": "All machines are adding one by one."}
    except Exception as error:
        print(error)


@fast_app.post("/add-blocks")
def add_blocks():
    try:
        for block in range(10):
            add_back_blocks.delay(block)
        return {"message": "All blocks are adding one by one."}
    except Exception as error:
        print(error)
