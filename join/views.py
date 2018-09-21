# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from login.models import User
from django.db.models import Q
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
        if User.objects.filter(mail=userMail).exists():
            return HttpResponse(json.dumps({'result': 'mail duplicated'}))
        else:
            user = User( name = userName, mail = userMail, password=userPwd, age = userAge, gender = userGender, region = userRegion, phonenumber = userPhoneNumber)
            user.save()
            return HttpResponse(json.dumps({'result': 'signup'}))


# 카카오톡 회원등록 join def
@csrf_exempt
def joinKakao(request):
    if request.method == "POST":
        userName = request.POST.get('userName')
        userMail = request.POST.get('userMail')
        userAge = request.POST.get('userAge')
        userGender= request.POST.get('userGender')
        userRegion = request.POST.get('userRegion')
        userPhoneNumber = request.POST.get('userPhoneNumber')
        userAccessToken = request.POST.get('userAccessToken')
        if User.objects.filter(mail=userMail).exists():
            return HttpResponse(json.dumps({'result': 'mail duplicated'}))
        user = User( name = userName, mail = userMail, age = userAge, gender = userGender, region = userRegion, phonenumber = userPhoneNumber, accesstoken_kakao = userAccessToken)
        user.save()
        return HttpResponse(json.dumps({'result': 'signup'}))



# 페이스북 회원등록 join def
@csrf_exempt
def joinFacebook(request):
    if request.method == "POST":
        userName = request.POST.get('userName')
        userMail = request.POST.get('userMail')
        userAge = request.POST.get('userAge')
        userGender= request.POST.get('userGender')
        userRegion = request.POST.get('userRegion')
        userPhoneNumber = request.POST.get('userPhoneNumber')
        userAccessToken = request.POST.get('userAccessToken')
        user = User( name = userName, mail = userMail, age = userAge, gender = userGender, region = userRegion, phonenumber = userPhoneNumber, accesstoken_facebook = userAccessToken)
        user.save()
        return HttpResponse(json.dumps({'result': 'signup'}))



# 회원정보 수정 def
@csrf_exempt
def modify(request):
    if request.method == "GET":
        userAccessToken = request.GET.get('userAccessToken')
        user = User.objects.filter(Q(accesstoken_itself=userAccessToken)|Q(accesstoken_kakao=userAccessToken)|Q(accesstoken_facebook=userAccessToken))
        return HttpResponse(json.dumps({'result': {
            'name': user.name,
            'age': user.age,
            'mail': user.mail,
            'password': user.password,
            'gender': user.gender,
            'region': user.region,
            'phonenumber': user.phonenumber,
            'introduce': user.introduce,
        }}))

    elif request.method == "POST":
        userName = request.POST.get('userName')
        userMail = request.POST.get('userMail')
        userAge = request.POST.get('userAge')
        userPwd = request.POST.get('userPwd')
        userPhoneNumber = request.POST.get('userPhoneNumber')
        userGender= request.POST.get('userGender')
        userRegion = request.POST.get('userRegion')
        userIntroduce = request.POST.get('userIntroduce')

        user = User.objects.get(mail=userMail)
        user.password=userPwd
        user.name=userName
        user.mail=userMail
        user.age=userAge
        user.phonenumber=userPhoneNumber
        user.region=userRegion
        user.gender=userGender
        user.introduce=userIntroduce
        user.save()
        return HttpResponse(json.dumps({'result': 'modify success'}))

# 회원정보 검색 def
@csrf_exempt
def search(request):
    if request.method == "POST":
        userId = request.POST.get('userId')
        return HttpResponse(json.dumps({'result': 'search success'}))
