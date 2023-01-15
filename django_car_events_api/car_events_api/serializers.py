from rest_framework import serializers
from .models import Blog
from .models import CarSpecs
from .models import CarPlan
from .models import Inventory


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'date', 'event_name',
                  'event_location', 'topic', 'post')


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('id', 'vendor_name', 'item_name',
                  'item_description', 'item_price', 'image_link')


class CarPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPlan
        fields = ('id', 'plan_name', 'year_of_warranty', 'finance_plan')


class CarSpecsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSpecs
        fields = ('id', 'car_plan', 'production_year', 'car_make',
                  'car_model', 'engine_type', 'image_link')

        depth = 1
