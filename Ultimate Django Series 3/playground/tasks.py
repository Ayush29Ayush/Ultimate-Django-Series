from time import sleep
from celery import shared_task


@shared_task(bind=True)
def test_func(self):
    # operations
    for i in range(10):
        print(i)
    return "Done"


@shared_task
def notify_customers(message):
    print("Sending 10k emails to customers...")
    print(message)
    sleep(10)
    print("Emails were successfully sent!!!")
