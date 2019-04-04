from django.contrib import admin
from .models import Blackspot
from .models import Landslide

admin.site.register(Blackspot)
admin.site.register(Landslide)