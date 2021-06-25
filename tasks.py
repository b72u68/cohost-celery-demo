from config import Config
from celery import Celery
from time import sleep

client = Celery("tasks",
                broker=Config.CELERY_BROKER_URL,
                backend=Config.CELERY_RESULT_BACKEND)


@client.task
def add(data):
    sleep(5)
    return data["first"] + data["second"]


@client.task
def subtract(data):
    sleep(5)
    return data["first"] - data["second"]


@client.task
def multiply(data):
    sleep(5)
    return data["first"] * data["second"]


@client.task
def divide(data):
    sleep(5)

    if data["second"] == 0:
        return "Error"

    return data["first"] / data["second"]
