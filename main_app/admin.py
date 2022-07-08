from django.contrib import admin

# Register your models here.
from .models import Gem, Polishing
admin.site.register(Gem)
admin.site.register(Polishing)
