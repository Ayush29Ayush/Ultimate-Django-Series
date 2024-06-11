from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product, Customer, Collection, OrderItem

# Create your views here.
#! request -> response
#! request handler
#! action of the view


def say_hello(request):

    queryset = Product.objects.only("id", "title", "unit_price")

    context = {"name": "Ayush", "products": list(queryset)}
    return render(request, "hello.html", context=context)
