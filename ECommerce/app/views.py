from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework import mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer, Product
from .serializer import CustomerSerializer, ProductSerializer
from django.utils import timezone

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductActivateDeactivateView(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def put(self, request, *args, **kwargs):
        product = self.get_object()
        # Check if the product was created more than 2 months ago
        if (timezone.now() - product.created_at).days >= 60:
            # Deactivate the product
            product.active = False
        else:
            # Activate the product
            product.active = True
        product.save()
        serializer = self.get_serializer(product)
        return Response(serializer.data)

