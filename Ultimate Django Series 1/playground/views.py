from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#! request -> response
#! request handler
#! action of the view


def say_hello(request):
    # return HttpResponse("Hello World")
    context = {"name": "Ayush"}
    return render(request, "hello.html", context=context)
