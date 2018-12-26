# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from store.models import Store
from store.models import StoreReview
from store.models import StoreShutdown
from login.models import User
from .models import Follow
from .models import WantToGo
from .models import CollectionList
from .models import Collection
import json

###
#   SNS 관련 뷰
#
#   @author brother Jun
###

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


# 작성한 리뷰 리스트 불러오기
@csrf_exempt
def callReview(request):
    if request.method == "GET":
        reviews = []
        userId = request.GET.get('userId')
        review_set = StoreReview.objects.filter(userid_id=userId)
        for review in review_set:
            userData = User.objects.get(id=review.userid_id)
            # userid_id를 통해 User테이블의 user 닉네임을 배열에 append하여야 함
            reviews.append(review.id)
            reviews.append(userData.id)
            reviews.append(userData.name)
            reviews.append(review.review)
            reviews.append(review.storepoint)
            # 리뷰간 구분을 위한 구분자 '#'
            reviews.append('#')

        return HttpResponse(json.dumps({'result': reviews}))

# 개인 SNS 공간(홈)으로 이동하기
@csrf_exempt
def callSnsHome(request):
    if request.method == "GET":
        return HttpResponse(json.dumps({'result': 'testok'}))


# 팔로우 리스트 불러오기
@csrf_exempt
def callFollow(request):
    if request.method == "GET":
        follow = []
        userId = request.GET.get('userId')
        user_set = Follow.objects.filter(userid_id=userId)
        for followUser in user_set:
            # 팔로우 한 유저의 정보를 보기 위해 User DB get
            # followid 컬럼은 fk가 아닌, charField이므로 mail이 저장되어있음
            userData = User.objects.get(mail=followUser.followid)
            follow.append(userData.id)
            follow.append(userData.name)
            follow.append(userData.age)
            follow.append(userData.gender)
            follow.append(userData.region)
            follow.append('#')

        return HttpResponse(json.dumps({'result': follow}))


# 팔로워 리스트 불러오기
@csrf_exempt
def callFollower(request):
    if request.method == "GET":
        follower = []
        userMail = request.GET.get('userMail')
        user_set = Follow.objects.filter(followid=userMail)
        for followerUser in user_set:
            # followerUser가 갖고 있는 userid_id를 통해 User DB 접근
            # User DB의 해당 컬럼이 갖고 있는 name, age등의 정보를 배열에 append
            userData = User.objects.get(id=followerUser.userid_id)
            follower.append(followerUser.userid_id)
            follower.append(userData.name)
            follower.append(userData.age)
            follower.append(userData.gender)
            follower.append(userData.region)
            follower.append('#')

        return HttpResponse(json.dumps({'result': follower}))


# 팔로우 추가하기
@csrf_exempt
def addFollow(request):
    if request.method == "POST":
        # user의 id와 follow하고자 하는 이의 id를 입력받음
        userId = request.POST.get('userId')
        followId = request.POST.get('followId')
        # follow id를 통해 follow의 mail주소를 얻어냄
        # Follow DB의 followid 컬럼은 외래키가 아닌 mail주소를 입력받기 때문임
        followUser = User.objects.get(id=followId)

        follow = Follow(followid=followUser.mail, userid_id=userId)
        follow.save()


        return HttpResponse(json.dumps({'result': 'added_follow'}))



# 개인 컬렉션 리스트 불러오기
@csrf_exempt
def callCollection(request):
    if request.method == "GET":
        listCollection =[]
        userMail = request.GET.get('userMail')

        user = User.objects.get(mail=userMail)
        userId = user.id

        collection_set = CollectionList.objects.filter(userid_id=userId)

        for collection in collection_set:
            listCollection.append(collection.collectionname)

        return HttpResponse(json.dumps({'result': listCollection }))


# 개인 컬렉션 리스트 삭제하기
# 해당 컬렉션 고유 id를 받아서 컬렉션 리스트 삭제
@csrf_exempt
def deleteCollection(request):
    if request.method == "POST":
        collectionId = request.POST.get('collectionId')
        del_col = CollectionList.objects.filter(id = collectionId)
        del_col.delete()
        return HttpResponse(json.dumps({'result': 'delete_collection'}))


# 개인 컬렉션 리스트 생성하기
@csrf_exempt
def createCollection(request):
    if request.method == "POST":
        # userMail과 생성할 컬렉션name을 받아오기
        userMail = request.POST.get('userMail')
        collectionName= request.POST.get('collectionName')

        #사용자 mail의 id값을 찾아내어 CollectionList의 userid_id에 삽입
        #collectionName은 그대로 CollectionList의 collectionname에 삽입
        user = User.objects.get(mail=userMail)
        userId = user.id

        collection = CollectionList(collectionname=collectionName, userid_id=userId)
        collection.save()

        return HttpResponse(json.dumps({'result': 'create_collection'}))




# 컬렉션 리스트 내 가게 리스트 불러오기
@csrf_exempt
def callCollectionList(request):
    if request.method == "GET":
        return HttpResponse(json.dumps({'result': listCollection }))

# 컬렉션 내 가게리스트 가게 추가하기
@csrf_exempt
def addCollectionList(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({'result': 'testok'}))

# 개인 컬렉션 리스트 삭제하기
@csrf_exempt
def deleteCollectionList(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({'result': 'testok'}))






# 가고싶은 가게 리스트 불러오기
@csrf_exempt
def callStoreList(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({'result': 'testok'}))


# 가고싶은 가게 리스트 저장하기
@csrf_exempt
def storageStoreList(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({'result': 'testok'}))

# 가고싶은 가게 리스트 삭제하기
@csrf_exempt
def deleteStoreList(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({'result': 'testok'}))