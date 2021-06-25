from celery import Celery

client = Celery("tasks")
client.config_from_object("celeryconfig")


@client.task
def add(data):
    return data["first"] + data["second"]


@client.task
def subtract(data):
    return data["first"] - data["second"]


@client.task
def multiply(data):
    return data["first"] * data["second"]


@client.task
def divide(data):
    if data["second"] == 0:
        return "Error"

    return data["first"] / data["second"]
