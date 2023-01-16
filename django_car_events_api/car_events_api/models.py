from django.db import models


# Create your models here.


class Blog(models.Model):
    date = models.CharField(max_length=20)
    name = models.CharField(max_length=32)
    location = models.CharField(max_length=60)
    topic = models.CharField(max_length=60)
    text = models.TextField(max_length=2000)


class Vendor(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Product(models.Model):
    vendor = models.ForeignKey(
        Vendor, on_delete=models.SET_NULL, null=True
    )
    category = models.ManyToManyField(
        Category
    )
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    price = models.CharField(max_length=20)
    image_link = models.CharField(max_length=255, blank=True)


class Option(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Car(models.Model):
    option = models.ForeignKey(
        Option, on_delete=models.SET_NULL, null=True
    )
    year = models.IntegerField()
    make = models.CharField(max_length=60)
    model = models.CharField(max_length=100)
    engine_type = models.CharField(max_length=50)
    image_link = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.model
