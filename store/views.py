# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import Store
from .models import StoreReview
from .models import StoreShutdown
from login.models import User
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
        if storeRegion != "" and storeReviewPoint == 1:
            store_set = Store.objects.filter(storename=storeName).filter(storeregion=storeRegion).order_by('storepoint')
            for store in store_set:
                listStore.append(store.id)
                listStore.append(store.storename)
                listStore.append(store.storeaddress)
                listStore.append(store.storeregion)
                listStore.append(store.storepoint)
                listStore.append(store.storelatitude)
                listStore.append(store.storelongitude)
                # store간 구분을 위해 특수문자 # 삽입(split할 것)
                listStore.append('#')

            return HttpResponse(json.dumps({'result': listStore}))

        # storeRegion 입력값이 있으면서 리뷰순을 정순으로 설정했을 떄.
        elif storeRegion != "" or storeReviewPoint == 0:
            store_set = Store.objects.filter(storename=storeName).filter(storeregion=storeRegion).order_by('-storepoint')
            for store in store_set:
                listStore.append(store.id)
                listStore.append(store.storename)
                listStore.append(store.storeaddress)
                listStore.append(store.storeregion)
                listStore.append(store.storepoint)
                listStore.append(store.storelatitude)
                listStore.append(store.storelongitude)
                # store간 구분을 위해 특수문자 # 삽입(split할 것)
                listStore.append('#')

            return HttpResponse(json.dumps({'result': listStore}))

        # storeRegion 입력값이 없으면서 역순 설정
        elif storeRegion == "" and storeReviewPoint == 1:
            store_set = Store.objects.filter(storename=storeName).order_by('storepoint')
            for store in store_set:
                listStore.append(store.id)
                listStore.append(store.storename)
                listStore.append(store.storeaddress)
                listStore.append(store.storeregion)
                listStore.append(store.storepoint)
                listStore.append(store.storelatitude)
                listStore.append(store.storelongitude)
                # store간 구분을 위해 특수문자 # 삽입(split할 것)
                listStore.append('#')

            return HttpResponse(json.dumps({'result': listStore}))

        # storeRegion 입력값이 없음. 리뷰순이 설정됐거나 기본
        elif storeRegion == "" or storeReviewPoint == 0:
            store_set = Store.objects.filter(storename=storeName).order_by('-storepoint')
            for store in store_set:
                listStore.append(store.id)
                listStore.append(store.storename)
                listStore.append(store.storeaddress)
                listStore.append(store.storeregion)
                listStore.append(store.storepoint)
                listStore.append(store.storelatitude)
                listStore.append(store.storelongitude)
                # store간 구분을 위해 특수문자 # 삽입(split할 것)
                listStore.append('#')

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
        userMail = request.POST.get('UserMail')
        storeId = request.POST.get('storeId')
        storeReview = request.POST.get('storeReview')
        storePoint = request.POST.get('storePoint')

        #받은 리뷰어의 메일과 같은 유저의 고유키를 USER db에서 꺼내옴
        reviewer = User.objects.filter(mail=userMail)

        storereview = StoreReview(review = storeReview, storeid_id = storeId, userid_id = reviewer.id, storepoint = storePoint)
        storereview.save()

        ## reviewer.id 가 쿼리셋에 없다고 나옴 --> 해당 내용 해결해야함


        return HttpResponse(json.dumps({'result': 'review_success'}))

    elif request.method == "GET":

        return HttpResponse(json.dumps({'result': 'testok'}))


# 가게가 사라졌어요 사용자 요청받기
@csrf_exempt
def shutdownStore(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({'result': 'testok'}))

# 가게 정보 추가하기(수정하기)
@csrf_exempt
def addStore(request):
    if request.method == "POST":
        storeName = request.POST.get('storeName')
        storeAddress = request.POST.get('storeAddress')
        storeRegion = request.POST.get('storeRegion')
        storePoint = request.POST.get('storePoint')
        storeLatitude = request.POST.get('storeLatitude')
        storeLongitude = request.POST.get('storeLongitude')

        store = Store( storename = storeName, storeaddress = storeAddress, storeregion = storeRegion, storepoint = storePoint, storelatitude = storeLatitude, storelongitude = storeLongitude)
        store.save()
        return HttpResponse(json.dumps({'result': 'insert_ok'}))


# 선택 지역 가게 리스트 불러오기
@csrf_exempt
def selectRegion(request):
    if request.method == "GET":
        listStore = []

        storeRegion = request.GET.get('storeRegion')

        # storepoint가 높은 순으로 출력됨
        store_set = Store.objects.filter(storeregion=storeRegion).order_by(
                '-storepoint')

        for store in store_set:
            listStore.append(store.id)
            listStore.append(store.storename)
            listStore.append(store.storeaddress)
            listStore.append(store.storeregion)
            listStore.append(store.storepoint)
            listStore.append(store.storelatitude)
            listStore.append(store.storelongitude)
            # store간 구분을 위해 특수문자 # 삽입(split할 것)
            listStore.append('#')

        return HttpResponse(json.dumps({'result': listStore}))
