from rest_framework import serializers
from .models import Blog
from .models import CarSpecs
from .models import CarPlan
from .models import Inventory


class BlogSerializer(serializers.Serializer):
    class Meta:
        model = Blog
        fields = ('id', 'date', 'event_name',
                  'event_location', 'topic', 'post')


class InventorySerializer(serializers.Serializer):
    class Meta:
        model = Inventory
        fields = ('id', 'vendor_name', 'item_name',
                  'item_description', 'item_price', 'image_link')


class CarSpecsSerializer(serializers.Serializer):
    plans = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='plan_name')

    class Meta:
        model = CarSpecs
        fields = ('id', 'plans', 'production_year', 'car_make',
                  'car_model', 'engine_type', 'image_link')
        # depth = 1


class CarPlanSerializer(serializers.Serializer):
    class Meta:
        model = CarPlan
        fields = ('id', 'plan_name', 'year_of_warranty', 'finance_plan')
