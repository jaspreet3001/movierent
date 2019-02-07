from django.contrib import admin
from django.contrib.auth.models import User
from .models import customer,movie,modelCustomer
# Register your models here.


admin.site.register(customer)
admin.site.register(movie)

