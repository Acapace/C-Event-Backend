from django.shortcuts import render
from drf_multiple_model.views import ObjectMultipleModelAPIView

# Create your views here.

from rest_framework import generics
from .serializers import BlogSerializer
from .serializers import InventorySerializer
from .serializers import CarPlanSerializer
from .serializers import CarSpecsSerializer

from .models import Blog
from .models import CarSpecs
from .models import CarPlan
from .models import Inventory

# / blog POST, GET


class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all().order_by('id')
    serializer_class = BlogSerializer

# /blog/:id - - - - and so on


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all().order_by('id')
    serializer_class = BlogSerializer


class InventoryList(generics.ListCreateAPIView):
    queryset = Inventory.objects.all().order_by('id')
    serializer_class = InventorySerializer


class InventoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all().order_by('id')
    serializer_class = InventorySerializer


class CarPlanList(generics.ListCreateAPIView):
    queryset = CarPlan.objects.all().order_by('id')
    serializer_class = CarPlanSerializer


class CarPlanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarPlan.objects.all().order_by('id')
    serializer_class = CarPlanSerializer


class CarSpecsList(generics.ListCreateAPIView):
    queryset = CarSpecs.objects.all().order_by('id')
    serializer_class = CarSpecsSerializer


class CarSpecsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarSpecs.objects.all().order_by('id')
    serializer_class = CarSpecsSerializer
