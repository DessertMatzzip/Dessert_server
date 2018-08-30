from django.db import models

# Create your models here.
class Store(models.Model):
    storename = models.CharField(max_length=200)
    storeaddress = models.CharField(max_length=200)


class StoreReview(models.Model):
    storeid = models.ForeignKey(Store, on_delete=models.CASCADE)
    review = models.CharField(max_length=200)