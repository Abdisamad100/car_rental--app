from django.contrib import admin
from .models import Profile, CarRental, CarReturn

admin.site.register(Profile)
admin.site.register(CarRental)
admin.site.register(CarReturn)
