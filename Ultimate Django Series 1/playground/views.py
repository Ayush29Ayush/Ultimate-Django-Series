from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product, Customer, Collection, OrderItem, Order

# Create your views here.
#! request -> response
#! request handler
#! action of the view


def say_hello(request):

    # selected_related (1)
    # prefetch_related (n)
    # queryset = Product.objects.prefetch_related("promotions").select_related("collection").all()
    queryset = Order.objects.all().order_by("-placed_at").select_related("customer").prefetch_related("orderitem_set__product")[:5]

    context = {"name": "Ayush", "orders": list(queryset)}
    return render(request, "hello.html", context=context)
