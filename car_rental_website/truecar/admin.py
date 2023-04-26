from django.contrib import admin

# Register your models here.

from . models import Product
from . models import Allcars
from . models import Hatchback
from . models import Sedan
from . models import Suv

admin.site.register(Product)
admin.site.register(Allcars)
admin.site.register(Hatchback)
admin.site.register(Sedan)
admin.site.register(Suv)

