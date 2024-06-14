from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Product, Customer, Collection, OrderItem, Order
from django.contrib.contenttypes.models import ContentType
from tags.models import Tag, TaggedItem

# Create your views here.
#! request -> response
#! request handler
#! action of the view


def say_hello(request):
    Collection.objects.filter(pk=11).update(title="Only Games", featured_product=None)

    context = {"name": "Ayush"}
    return render(request, "hello.html", context=context)
