from django.db import models
from login.models import User
from store.models import Store
# Create your models here.


class CollectionList(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    collectionname= models.CharField(max_length=200)


class Collection(models.Model):
    collectid= models.ForeignKey(CollectionList, on_delete=models.CASCADE)
    storeid= models.ForeignKey(Store, on_delete=models.CASCADE)


class WantToGo(models.Model):
    wantstoreid= models.ForeignKey(Store, on_delete=models.CASCADE)
    userid= models.ForeignKey(User, on_delete=models.CASCADE)


class Follow(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    followid = models.CharField(max_length=200)