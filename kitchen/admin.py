from django.contrib import admin

from kitchen.models import DishType, Cook, Dish


admin.site.register(DishType)
admin.site.register(Dish)
admin.site.register(Cook)