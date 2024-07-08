from django.shortcuts import render
from playground.tasks import notify_customers


def say_hello(request):
    notify_customers.delay(message="Hello World")
    return render(request, 'hello.html', {'name': 'Ayush Senapati'})
