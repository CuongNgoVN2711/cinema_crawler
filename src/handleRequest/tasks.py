from celery import shared_task


@shared_task
def run_double(number):
    double = number * 2
    return double
