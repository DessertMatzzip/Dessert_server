# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from random import *
from string import *
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

# 작동원리
    # 1. login url로 accessToken을 파라미터로 갖으면서 로그인 시도
    # 2. 해당 accessToken이 DB에 있는지 search함.
    # 3. accessToken이 DB에 있을 경우 기존 사용자이므로, 메인 액티비티로 전환하면 됨.
    #    그러나 accessToken이 DB에 없으면 신규가입자이므로, 가입 약관 액티비티로 이동시킴.
    # 4. 신규가입자에게 정보동의를 얻고 해당 Token과 사용자의 정보를 DB에 저장.

    # 5. 자체로그인의 경우 id와 pwd가 디비에 있는지 확인. 있다면 로그인 신호 넘겨줌.

# facebook accesstoken db 확인
@csrf_exempt
def loginFacebook(request):
    if request.method == "POST":
        accessToken = request.POST.get('accessToken')
        if User.objects.filter(accesstoken_facebook=accessToken).exists():
            return HttpResponse(json.dumps({'result': 'signin_req'}))
        else:
            return HttpResponse(json.dumps({'result': 'signup_req'}))


# kakao accesstoken db 확인
@csrf_exempt
def loginKakao(request):
    if request.method == "POST":
        accessToken = request.POST.get('accessToken')
        if User.objects.filter(accesstoken_kakao=accessToken).exists():
            return HttpResponse(json.dumps({'result': 'signin_req'}))
        else:
            return HttpResponse(json.dumps({'result': 'signup_req'}))


# 자체 로그인, email(id)와 pwd를 db에서 확인
@csrf_exempt
def loginItself(request):
    if request.method == "POST":
        mail = request.POST.get('loginEmail')
        password = request.POST.get('loginPwd')
        if User.objects.filter(mail=mail).exists():
            if User.objects.filter(password=password).exists():
                return HttpResponse(json.dumps({'result':'signin_req'}))
            else:
                return HttpResponse(json.dumps({'result': 'error_pwd'}))
        else:
            return HttpResponse(json.dumps({'result':'error_email'}))
    elif request.method =="GET":
        accesstoken = request.POST.get('userAccessToken')
        import string, random
        passkey = ''
        for x in range(10):
            if random.choice([1, 2]) == 1:
                passkey += passkey.join(random.choice(string.ascii_letters))
            else:
                passkey += passkey.join(random.choice(string.digits))
            accesstoken = passkey
        return HttpResponse(json.dumps({'result': passkey}))