from django.db import models
from login.models import User

# Create your models here.
class Store(models.Model):
    storename = models.CharField(max_length=200)
    storeaddress = models.CharField(max_length=200)
    storeregion = models.CharField(max_length=200, default="charField")
    storepoint = models.CharField(max_length=200, default="0")
    storelatitude = models.CharField(max_length=200, default="176.4")
    storelongitude = models.CharField(max_length=200, default="-145.3")

class StoreReview(models.Model):
    storeid = models.ForeignKey(Store, on_delete=models.CASCADE)
    review = models.CharField(max_length=200)
    storepoint = models.CharField(max_length=200, default="0")
    userid = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

class StoreShutdown(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    storeid = models.ForeignKey(Store, on_delete=models.CASCADE)
    review = models.CharField(max_length=200)
