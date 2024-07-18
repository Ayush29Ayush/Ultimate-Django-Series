from django.shortcuts import render
import requests
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.views import APIView

# @cache_page(5 * 60)
# def say_hello(request):
#     response = requests.get("http://httpbin.org/delay/2")
#     data = response.json()
#     return render(request, "hello.html", {"name": data})

class HelloView(APIView):
    @method_decorator(cache_page(5 * 60)) #! We cannot utilize decorators directly on class based views so we use method_decorator
    def get(self, request):
        response = requests.get("http://httpbin.org/delay/2")
        data = response.json()
        return render(request, "hello.html", {"name": "Ayush Senapati"})
