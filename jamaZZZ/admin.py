from django.contrib import admin
from .models import UserProfile, Items, ProductWomen, Men,Design, Cart

# Register your models here.
admin.site.register([UserProfile, Items, ProductWomen, Men,Design, Cart])
