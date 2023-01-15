from django.db import models


# Create your models here.


class Blog(models.Model):
    date = models.CharField(max_length=20)
    event_name = models.CharField(max_length=32)
    event_location = models.CharField(max_length=60)
    topic = models.CharField(max_length=60)
    post = models.TextField(max_length=2000)


class Inventory(models.Model):
    vendor_name = models.CharField(max_length=60)
    item_name = models.CharField(max_length=60)
    item_description = models.CharField(max_length=200)
    item_price = models.CharField(max_length=20)
    image_link = models.CharField(max_length=255, blank=True)


class CarSpecs(models.Model):
    # car_plan = models.ForeignKey(
    #     CarPlan, on_delete=models.SET_NULL, null=True)
    production_year = models.IntegerField()
    car_make = models.CharField(max_length=60)
    car_model = models.CharField(max_length=100)
    engine_type = models.CharField(max_length=50)
    image_link = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.car_model


class CarPlan(models.Model):
    car_specs = models.ForeignKey(
        CarSpecs, related_name='plans', on_delete=models.CASCADE, null=True)
    plan_name = models.CharField(max_length=20)
    year_of_warranty = models.PositiveBigIntegerField(default=1)
    finance_plan = models.CharField(max_length=20, default="unavailable")

    def __str__(self):
        return self.plan_name
