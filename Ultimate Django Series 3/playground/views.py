from django.shortcuts import render
import requests
import logging
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.views import APIView

# Approach - 1 (Basic)
# logger = logging.getLogger("playground.views") #! This will make a new logger with name 'playground.views'

# Approach - 2 (Optimized)
logger = logging.getLogger(
    __name__
)  #! This will make a new logger with name 'playground.views' dynamically according to the file name


class HelloView(APIView):
    def get(self, request):
        try:
            logger.info("Calling httpbin.org/delay/2")
            response = requests.get("http://httpbin.org/delay/2")
            logger.info("Received response from httpbin.org/delay/2")
            data = response.json()
        except requests.ConnectionError:
            logger.critical("httpbin is offline. Could not connect to httpbin.org/delay/2")
        return render(request, "hello.html", {"name": "Ayush Senapati"})
