# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from login.models import User
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

# 작동원리
    # 1. 자체회원가입 버튼 클릭시 editText의 회원정보들을 DB에 입력

    # 2. (회원정보 수정 시) 회원정보 수정 버튼 클릭시 editText의 회원정보들을 DB에 갱신

# 자체회원등록 join def
@csrf_exempt
def joinItself(request):
    if request.method == "POST":
        userId = request.POST.get('userId', '')
        userName = request.POST.get('userName', '')
        userMail = request.POST.get('userMail', '')
        userAge = request.POST.get('userAge', '')
        userPhoneNumber = request.POST.get('userPhoneNumber', '')
        userAccessToken = request.POST.get('userAccessToken', '')
        user = User( userid = userId, name = userName, mail = userMail, age = userAge, phonenumber = userPhoneNumber, accesstoken_itself = userAccessToken)
        user.save()
        return HttpResponse(json.dumps({'result': 'signup'}))


# 카카오톡 회원등록 join def
@csrf_exempt
def joinKakao(request):
    if request.method == "POST":
        userId = request.POST.get('userId', '')
        userName = request.POST.get('userName', '')
        userMail = request.POST.get('userMail', '')
        userAge = request.POST.get('userAge', '')
        userPhoneNumber = request.POST.get('userPhoneNumber', '')
        userAccessToken = request.POST.get('userAccessToken', '')
        user = User( userid = userId, name = userName, mail = userMail, age = userAge, phonenumber = userPhoneNumber, accesstoken_itself = userAccessToken)
        user.save()
        return HttpResponse(json.dumps({'result': 'signup'}))



# 페이스북 회원등록 join def
@csrf_exempt
def joinFacebook(request):
    if request.method == "POST":
        userId = request.POST.get('userId', '')
        userName = request.POST.get('userName', '')
        userMail = request.POST.get('userMail', '')
        userAge = request.POST.get('userAge', '')
        userPhoneNumber = request.POST.get('userPhoneNumber', '')
        userAccessToken = request.POST.get('userAccessToken', '')
        user = User( userid = userId, name = userName, mail = userMail, age = userAge, phonenumber = userPhoneNumber, accesstoken_itself = userAccessToken)
        user.save()
        return HttpResponse(json.dumps({'result': 'signup'}))



# 회원정보 수정 def
@csrf_exempt
def modify(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({'result': 'modify success'}))

