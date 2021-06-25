from celery import Celery
from time import sleep

client = Celery("tasks")
client.config_from_object("celeryconfig")


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
