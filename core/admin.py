from django.contrib import admin

# Register your models here.
from .models import UserData, RevenueSpending

admin.site.register(UserData)
admin.site.register(RevenueSpending)