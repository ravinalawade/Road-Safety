from django.contrib import admin
from .models import Blackspot
from .models import Landslide
from .models import Update

admin.site.register(Blackspot)
admin.site.register(Landslide)
admin.site.register(Update)