# -*- coding: utf-8 -*-
from django.db import models

# 사용자 정보 테이블(이름, 이메일, 나이)
class User(models.Model):
    name = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    accesstoken = models.CharField(max_length=200, default="charField")