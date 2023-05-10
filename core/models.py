from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=16, null=False)
    balance = models.FloatField(default=0.0)
    # image = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.name
    

class RevenueSpending(models.Model):
    IS_REVENUE = [
        ('0', 'Revenue'),
        ('1', 'Spending')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    about = models.CharField(max_length=150, null=False)
    date = models.DateTimeField(auto_created=True)
    value = models.FloatField(null=False)
    type = models.CharField(max_length=1, choices=IS_REVENUE, null=False)
    def __str__(self):
        return self.name