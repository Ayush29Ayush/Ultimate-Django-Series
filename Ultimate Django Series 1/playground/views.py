from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#! request -> response
#! request handler
#! action of the view


def calculate():
    x = 1
    y = 2
    return x+y

def say_hello(request):
    # return HttpResponse("Hello World")
    # x = 1
    # y = 2
    sum = calculate()
    context = {"name": "Ayush"}
    return render(request, "hello.html", context=context)
