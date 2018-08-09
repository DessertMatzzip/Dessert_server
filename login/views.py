# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

# 작동원리
    # 1. login url로 accessToken을 파라미터로 갖으면서 로그인 시도
    # 2. 해당 accessToken이 DB에 있는지 search함.
    # 3. accessToken이 DB에 있을 경우 기존 사용자이므로, 메인 액티비티로 전환하면 됨.
    #    그러나 accessToken이 DB에 없으면 신규가입자이므로, 가입 약관 액티비티로 이동시킴.
    # 4. 신규가입자에게 정보동의를 얻고 해당 Token과 사용자의 정보를 DB에 저장.

@csrf_exempt
def index(request):
    if request.method == "POST":
        accessToken = request.POST['accessToken']
        if accessToken in User.objects.all():
            return HttpResponse(json.dumps({'result': 'signin_req'}))
        else:
            return HttpResponse(json.dumps({'result': 'signup_req'}))
