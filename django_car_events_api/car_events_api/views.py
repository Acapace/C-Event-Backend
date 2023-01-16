from django.shortcuts import render
from drf_multiple_model.views import ObjectMultipleModelAPIView

# Create your views here.

from rest_framework import generics
from .serializers import BlogSerializer, VendorSerializer, CategorySerializer, ProductSerializer, OptionSerializer, CarSerializer

from .models import Blog, Vendor, Category, Option, Product, Car

# / blog POST, GET


class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all().order_by('id')
    serializer_class = BlogSerializer

# /blog/:id - - - - and so on


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all().order_by('id')
    serializer_class = BlogSerializer


class VendorList(generics.ListCreateAPIView):
    queryset = Vendor.objects.all().order_by('id')
    serializer_class = VendorSerializer


class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all().order_by('id')
    serializer_class = VendorSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer


class OptionList(generics.ListCreateAPIView):
    queryset = Option.objects.all().order_by('id')
    serializer_class = OptionSerializer


class OptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Option.objects.all().order_by('id')
    serializer_class = OptionSerializer


class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all().order_by('id')
    serializer_class = CarSerializer


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all().order_by('id')
    serializer_class = CarSerializer
