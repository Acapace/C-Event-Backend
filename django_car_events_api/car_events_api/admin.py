from django.contrib import admin
from .models import Blog
from .models import CarSpecs
from .models import CarPlan
from .models import Inventory


# Register your models here.

admin.site.register(Blog)

admin.site.register(Inventory)

admin.site.register(CarPlan)

admin.site.register(CarSpecs)
