from .celery import app


@app.task
def sum_integers_from_pro(x, y):
    return x + y