# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from login.models import User
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

# 작동원리
    # 1. 회원가입 버튼 클릭시 editText의 회원정보들을 DB에 입력

    # 2. (회원정보 수정 시) 회원정보 수정 버튼 클릭시 editText의 회원정보들을 DB에 갱신

# 회원등록 join def
@csrf_exempt
def join(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({'result': 'signup'}))


# 회원정보 수정 def
@csrf_exempt
def modify(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({'result': 'modify success'}))

