from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Count
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from store.models import Collection, OrderItem, Product, Review
from store.serializers import CollectionSerializer, ProductSerializer, ReviewSerializer
from pprint import pprint


class ProductViewSet(ModelViewSet):
    # queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        pprint(self)
        queryset = Product.objects.all()
        # collection_id = self.request.query_params['collection_id']
        collection_id = self.request.query_params.get('collection_id')
        
        if collection_id is not None:
            queryset = queryset.filter(collection_id=collection_id)
        
        return queryset
    
    def get_serializer_context(self):
        return {"request": self.request}
    
    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response(
                {
                    "error": "Product cannot be deleted because it is associated with an order item."
                }
            )
        return super().destroy(request, *args, **kwargs)


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(products_count=Count("products")).all()
    serializer_class = CollectionSerializer
    
    def get_serializer_context(self):
        return {"request": self.request}
    
    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(collection_id=kwargs['pk']).count() > 0:
            return Response(
                {
                    "error": "Collection cannot be deleted because it includes one or more products."
                }
            )
            
        return super().destroy(request, *args, **kwargs)


class ReviewViewSet(ModelViewSet):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    #! This is same as defining queryset but since we want the Reviews to be filtered acc to the pk, we will overwrite the default get_queryset()
    def get_queryset(self):
        # print(self.kwargs)
        return Review.objects.filter(product_id=self.kwargs["product_pk"])
    
    #! Since we do not want to pass the product id manually and want it to be taken from the url, pass the url details as context
    def get_serializer_context(self):
        print(self.kwargs)
        return {"product_id": self.kwargs["product_pk"]}