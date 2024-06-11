from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from store.models import Product, Customer, Collection, OrderItem

# Create your views here.
#! request -> response
#! request handler
#! action of the view


def say_hello(request):

    # queryset = Product.objects.filter(inventory__lt=10, unit_price__lt=20)
    queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))

    context = {"name": "Ayush", "products": list(queryset)}
    return render(request, "hello.html", context=context)