from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Product, Customer, Collection, OrderItem, Order

# Create your views here.
#! request -> response
#! request handler
#! action of the view


def say_hello(request):
    increased_price_by_ayush = ExpressionWrapper(F('unit_price') * 1.1, output_field=DecimalField())
    result = Product.objects.annotate(increased_price_by_ayush=increased_price_by_ayush)  

    context = {"name": "Ayush", "result": list(result)}
    return render(request, "hello.html", context=context)
