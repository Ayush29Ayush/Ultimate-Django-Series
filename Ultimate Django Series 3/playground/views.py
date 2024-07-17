from django.shortcuts import render
import requests

def say_hello(request):
    #! This will get you the response after 2 seconds of request
    requests.get("http://httpbin.org/delay/2")
    return render(request, "hello.html", {"name": "Ayush Senapati"})
