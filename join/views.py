# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from login.models import User
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

# 작동원리
    # 1. 자체회원가입 버튼 클릭시 editText의 회원정보들을 DB에 입력

    # 2. (회원정보 수정 시) 액세스 토큰값을 비교하여 해당 테이블의 회원 선택
    # 3.  회원정보 수정 버튼 클릭시 editText의 회원정보들을 DB에 갱신

# 자체회원등록 join def
@csrf_exempt
def joinItself(request):
    if request.method == "POST":
        userName = request.POST.get('userName')
        userMail = request.POST.get('userMail')
        userPwd = request.POST.get('userPwd')
        userAge = request.POST.get('userAge')
        userGender= request.POST.get('userGender')
        userRegion = request.POST.get('userRegion')
        userPhoneNumber = request.POST.get('userPhoneNumber')
        userAccessToken // 랜덤생성
        user = User( name = userName, mail = userMail, password=userPwd, age = userAge, gender = userGender, region = userRegion, phonenumber = userPhoneNumber)

        user.save()
        return HttpResponse(json.dumps({'result': 'signup'}))


# 카카오톡 회원등록 join def
@csrf_exempt
def joinKakao(request):
    if request.method == "POST":
        userId = request.POST.get('userId')
        userName = request.POST.get('userName')
        userMail = request.POST.get('userMail')
        userAge = request.POST.get('userAge')
        userGender= request.POST.get('userGender')
        userRegion = request.POST.get('userRegion')
        userPhoneNumber = request.POST.get('userPhoneNumber')
        userAccessToken = request.POST.get('userAccessToken')
        user = User( userid = userId, name = userName, mail = userMail, age = userAge, gender = userGender, region = userRegion, phonenumber = userPhoneNumber, accesstoken_kakao = userAccessToken)
        user.save()
        return HttpResponse(json.dumps({'result': 'signup'}))



# 페이스북 회원등록 join def
@csrf_exempt
def joinFacebook(request):
    if request.method == "POST":
        userId = request.POST.get('userId')
        userName = request.POST.get('userName')
        userMail = request.POST.get('userMail')
        userAge = request.POST.get('userAge')
        userGender= request.POST.get('userGender')
        userRegion = request.POST.get('userRegion')
        userPhoneNumber = request.POST.get('userPhoneNumber')
        userAccessToken = request.POST.get('userAccessToken')
        user = User( userid = userId, name = userName, mail = userMail, age = userAge, gender = userGender, region = userRegion, phonenumber = userPhoneNumber, accesstoken_facebook = userAccessToken)
        user.save()
        return HttpResponse(json.dumps({'result': 'signup'}))



# 회원정보 수정 def
@csrf_exempt
def modify(request):
    if request.method == "POST":
        userId = request.POST.get('userId')
        userName = request.POST.get('userName')
        userMail = request.POST.get('userMail')
        userAge = request.POST.get('userAge')
        userPhoneNumber = request.POST.get('userPhoneNumber')
        userGender= request.POST.get('userGender')
        userRegion = request.POST.get('userRegion')

        user = User.objects.get(userid=userId)
        user.name=userName
        user.mail=userMail
        user.age=userAge
        user.phonenumber=userPhoneNumber
        user.region=userRegion
        user.Gender=userGender

        user.save()

        return HttpResponse(json.dumps({'result': 'modify success'}))

