# -*- coding: utf-8 -*-
from django.db import models

# 사용자 정보 테이블(이름, 이메일, 나이)
class User(models.Model):
    name = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    accesstoken_facebook = models.CharField(max_length=200, default="charField")
    accesstoken_kakao = models.CharField(max_length=200, default="charField")
    accesstoken_itself = models.CharField(max_length=200, default="charField")