# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from  rest_framework.decorators import action

# from rest_framework.pagination import PageNumberPagination
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
)

# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response

# from rest_framework.views import APIView
# from rest_framework import status
from store.models import (
    Cart,
    CartItem,
    Collection,
    Customer,
    OrderItem,
    Product,
    Review,
)
from store.serializers import (
    AddCartItemSerializer,
    CartItemSerializer,
    CartSerializer,
    CollectionSerializer,
    CustomerSerializer,
    ProductSerializer,
    ReviewSerializer,
    UpdateCartItemSerializer,
)
from store.filters import ProductFilter
from store.pagination import DefaultPagination
from store.permissions import IsAdminOrReadOnly
from pprint import pprint


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ["title", "description"]
    ordering_fields = ["unit_price", "last_update"]
    # pagination_class = PageNumberPagination
    pagination_class = DefaultPagination
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_context(self):
        return {"request": self.request}

    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs["pk"]).count() > 0:
            return Response(
                {
                    "error": "Product cannot be deleted because it is associated with an order item."
                }
            )
        return super().destroy(request, *args, **kwargs)


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(products_count=Count("products")).all()
    serializer_class = CollectionSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_context(self):
        return {"request": self.request}

    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(collection_id=kwargs["pk"]).count() > 0:
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


# ? ModelViewSet: A viewset that provides default create(), retrieve(), update(), partial_update(), destroy() and list() actions.
#! Since we only need operations like "Creating a cart", "Getting a cart", "Deleting a cart" using POST, GET using id and DELETE methods, we will not use ModelViewSet because it will provide us with list and update methods which will expose all our data in the API. To prevent this, we will create a custom ViewSet.
# TODO : Create a custom ViewSet by combining various mixins and generic view set. Click on "ModelViewSet" using "Ctrl+Click" to see its implementation.
# class CartViewSet(ModelViewSet):
class CartViewSet(
    CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet
):
    # * CreateModelMixin: Used to create a model instance using POST method.
    # * RetrieveModelMixin: Used to retrieve a model instance using GET method.
    queryset = Cart.objects.prefetch_related("items__product").all()
    serializer_class = CartSerializer


#! Getting and Updating Cart Items
class CartItemViewSet(ModelViewSet):
    http_method_names = ["get", "post", "patch", "delete"]
    # queryset = CartItem.objects.all()
    # serializer_class = CartItemSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return AddCartItemSerializer
        elif self.request.method == "PATCH":
            return UpdateCartItemSerializer
        return CartItemSerializer

    def get_serializer_context(self):
        return {"cart_id": self.kwargs["cart_pk"]}

    def get_queryset(self):
        return CartItem.objects.filter(cart_id=self.kwargs["cart_pk"]).select_related(
            "product"
        )


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]
    
    #! Here we are overwriting the get_permissions() method according to the request method
    # def get_permissions(self):
    #     if self.request.method == "GET":
    #         return [AllowAny()]
    #     return [IsAuthenticated()]

    #! If the user is authenticated, we will get USER instance else AnonymousUser instance
    @action(detail=False, methods=["GET", "PUT"], permission_classes=[IsAuthenticated])
    def me(self, request):
        (customer, created) = Customer.objects.get_or_create(user_id=request.user.id)
        if request.method == "GET":
            print(request.user)
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method == "PUT":
            serializer = CustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        
