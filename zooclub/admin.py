from django.contrib import admin

from .models import OwnerModel, PetModel

# Register your models here.
admin.site.register(OwnerModel)
admin.site.register(PetModel)
