from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.

class Deposit(models.Model):
    deposited_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="deposited_by")
    amount = models.IntegerField(default=0)
    deposit_date = models.DateTimeField('deposit_date')
    
    def __str__(self):
        return f"{self.amount} From {self.deposited_by} On {self.deposit_date }"
