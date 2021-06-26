from config import Config
from celery import Celery
from time import sleep

client = Celery("tasks",
                broker=Config.CELERY_BROKER_URL,
                backend=Config.CELERY_RESULT_BACKEND)


@client.task
def add(x, y):
    sleep(1)
    return x + y


@client.task
def subtract(x, y):
    sleep(1)
    return x - y


@client.task
def multiply(x, y):
    sleep(1)
    return x * y


@client.task
def divide(x, y):
    sleep(1)

    if y == 0:
        return "Error"

    return x / y
