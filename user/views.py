# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.

# 작동원리
# 1. 팔로우 리스트 불러오기
# 2. 팔로우 테이블에서 (유저id+팔로우한 id)를 통해 팔로우 id 내어주기

# 3. 팔로워 리스트 불러오기
# 4. 팔로워 테이블에서 (팔로우당한 id+유저id)를 통해 유저 id 내어주기

# 5. 개인 컬렉션 리스트 불러오기
# 6. 컬렉션 테이블에서 (유저id+컬렉션이름)를 통해 컬렉션 이름 파악. 컬렉션 이름을 통해 해당 컬렉션 내 가게 리스트 불러오기 (이중 테이블 구조)

# 7. 개인 컬렉션 리스트 저장하기(삭제하기)
# 8. 해당 컬렉션에 존재하는 가게 리스트에서 추가, 삭제하기

# +. 개인 컬렉션 리스트 생성하기
# +. 가게정보들을 담을 컬렉션 리스트 생성하기(유저id+컬렉션 이름)에서 컬렉션 이름이 중복되지 않게 생성

# 9. 가고싶은 가게 리스트 불러오기
# 10. 가고싶은 가게 테이블에서 (유저id+가게id)를 통해 가게 정보 내어주기

# 11. 가고싶은 가게 리스트 저장하기(삭제하기)
# 12. 가고싶은 가게 테이블에서 (유저id+가게id)를 추가, 삭제하기

# 팔로우 리스트 불러오기
@csrf_exempt
def callFollow(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({'result': 'testok'}))


# 팔로워 리스트 불러오기
@csrf_exempt
def callFollower(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({'result': 'testok'}))


# 개인 컬렉션 리스트 불러오기
@csrf_exempt
def callCollection(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({'result': 'testok'}))


# 개인 컬렉션 리스트내 가게정보 저장하기(삭제하기)
@csrf_exempt
def storageCollection(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({'result': 'testok'}))


# 개인 컬렉션 리스트 생성하기
@csrf_exempt
def createCollection(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({'result': 'testok'}))


# 가고싶은 가게 리스트 불러오기
@csrf_exempt
def callStoreList(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({'result': 'testok'}))


# 가고싶은 가게 리스트 저장하기(삭제하기)
@csrf_exempt
def storageStoreList(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({'result': 'testok'}))