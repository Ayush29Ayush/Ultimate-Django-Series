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
from store.models import Collection, OrderItem, Product
from store.serializers import CollectionSerializer, ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
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
    
    # def delete(self, request, pk):
    #     product = get_object_or_404(Product, pk=pk)
    #     if product.orderitems.count() > 0:
    #         return Response(
    #             {
    #                 "error": "Product cannot be deleted because it is associated with an order item."
    #             },
    #             status=status.HTTP_405_METHOD_NOT_ALLOWED,
    #         )
    #     product.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


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
    
    # def delete(self, request, pk):
    #     collection = get_object_or_404(
    #         Collection.objects.annotate(products_count=Count("products")).all(), pk=pk
    #     )
    #     if collection.products_count > 0:
    #         return Response(
    #             {
    #                 "error": "Collection cannot be deleted because it includes one or more products."
    #             },
    #             status=status.HTTP_405_METHOD_NOT_ALLOWED,
    #         )
    #     collection.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
