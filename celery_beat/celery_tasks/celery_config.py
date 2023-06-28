from celery import Celery

celery_app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

########################################################################################################################
# These are the settings for celery beat
# celery_app.conf.beat_schedule = {
#     'send_hello_function': {
#         'task': 'task_scheduler.send_hello',
#         'schedule': timedelta(seconds=3),
#     },
# }

# Start the Celery beat scheduler
# celery_app.conf.timezone = 'UTC'
########################################################################################################################

# Define task routes
celery_app.conf.task_routes = {
    "celery_tasks.machine_tasks.add_back_machines": {"queue": "add_machines"},
    "celery_tasks.machine_tasks.add_back_blocks": {"queue": "add_blocks"},
}

# This is used when a celery app is configured using a class.
# celery_app.config_from_object('celery_config.celery_config')

celery_app.autodiscover_tasks(['celery_tasks.block_tasks', 'celery_tasks.machine_tasks'])
celery_app.conf.result_expires = 259200

