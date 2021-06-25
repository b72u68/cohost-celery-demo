from celery import Celery
from time import sleep

client = Celery("tasks")
client.config_from_object("celeryconfig")


@client.task
def add(data):
    sleep(5)
    return data["first"] + data["second"]
