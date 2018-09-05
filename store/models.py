from django.db import models
from login.models import User

# Create your models here.
class Store(models.Model):
    storename = models.CharField(max_length=200)
    storeaddress = models.CharField(max_length=200)
    storeregion = models.CharField(max_length=200, default="charField")


class StoreReview(models.Model):
    storeid = models.ForeignKey(Store, on_delete=models.CASCADE)
    review = models.CharField(max_length=200)
    userid = models.ForeignKey(User, on_delete=models.CASCADE, default=999)
