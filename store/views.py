# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import Store
from .models import StoreReview
from .models import StoreShutdown
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

# 작동원리
# 1. 가게 데이터 불러오기
# 2. 가게테이블에서 해당 필터를 적용하여 select해서 내어주기, orderby또한 필터적용

# 3. 가게 데이터 수정(요청받기)
# 4. 가게 정보 요청을 별도의 테이블로 받음. (유저 id+가게 id+가게점주 인증이미지+수정할 정보 텍스트)

# 5. 가게별 리뷰저장
# 6. 해당 유저가 리뷰를 남김. 별도의 리뷰 테이블에 (유저 id+가게 id+리뷰) 형태로 저장, 유저 아이디와 가게 아이디를 외래키 적용

# 7. 가게가 사라졌어요 요청받기
# 8. 가게가 사라졌다는 요청을 별도의 테이블로 받음. (유저 id+가게 id)

# 가게 데이터 불러오기
@csrf_exempt
def callStore(request):
    if request.method == "GET":

        listStore = []

        storeName = request.GET.get('storeName')
        storeRegion = request.GET.get('storeRegion')
        storeReviewPoint = request.GET.get('storeReviewPoint')

        # storeRegion의 입력값이 있음. 또한 리뷰순을 역순서 필터적용
        if storeRegion != null & storeReviewPoint == 1:
            store_set = Store.objects.filter(storename=storeName).orderby('-storepoint').filter(storeregion=storeRegion)
            for store in store_set:
                listStore.append(store.storename)
                listStore.append(store.storeaddress)
                listStore.append(store.storeregion)
                listStore.append(store.storepoint)
                listStore.append(store.storelatitude)
                listStore.append(store.storelongitude)
                # store간 구분을 위해 특수문자 # 삽입(split할 것)
                listUser.append('#')

            return HttpResponse(json.dumps({'result': listStore}))

        # storeRegion 입력값이 있으면서 리뷰순을 역순으로 설정했을 떄.
        elif storeRegion != null | storeReviewPoint == 0:
            store_set = Store.objects.filter(storename=storeName).orderby('storepoint').filter(storeregion=storeRegion)
            for store in store_set:
                listStore.append(store.storename)
                listStore.append(store.storeaddress)
                listStore.append(store.storeregion)
                listStore.append(store.storepoint)
                listStore.append(store.storelatitude)
                listStore.append(store.storelongitude)
                # store간 구분을 위해 특수문자 # 삽입(split할 것)
                listUser.append('#')

            return HttpResponse(json.dumps({'result': listStore}))

        # storeRegion 입력값이 없으면서 역순 설정
        elif storeRegion == null & storeReviewPoint == 1:
            store_set = Store.objects.filter(storename=storeName).orderby('-storepoint')
            for store in store_set:
                listStore.append(store.storename)
                listStore.append(store.storeaddress)
                listStore.append(store.storeregion)
                listStore.append(store.storepoint)
                listStore.append(store.storelatitude)
                listStore.append(store.storelongitude)
                # store간 구분을 위해 특수문자 # 삽입(split할 것)
                listUser.append('#')

            return HttpResponse(json.dumps({'result': listStore}))

        # storeRegion 입력값이 없음.
        elif storeRegion == null & storeReviewPoint == 0:
            store_set = Store.objects.filter(storename=storeName).orderby('storepoint')
            for store in store_set:
                listStore.append(store.storename)
                listStore.append(store.storeaddress)
                listStore.append(store.storeregion)
                listStore.append(store.storepoint)
                listStore.append(store.storelatitude)
                listStore.append(store.storelongitude)
                # store간 구분을 위해 특수문자 # 삽입(split할 것)
                listUser.append('#')

            return HttpResponse(json.dumps({'result': listStore}))




# 가게 데이터 수정(요청받기)
@csrf_exempt
def modifyStore(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({'result': 'testok'}))


# 가게별 리뷰저장
@csrf_exempt
def commentStore(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({'result': 'testok'}))


# 가게가 사라졌어요 사용자 요청받기
@csrf_exempt
def shutdownStore(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({'result': 'testok'}))