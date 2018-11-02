# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from store.models import Store
from store.models import StoreReview
from login.models import User
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

# 작동원리
    # 1. 지역별 리뷰어 랭킹 불러오기
    # 2. review중 (사람id+지역) 리뷰가 가장 많은 사람으로 orderby하고 순서대로 내어주기

    # 3. 지역별 가게 별점순 랭킹 불러오기
    # 4. review중 (가게id+지역) 별점평균이 가장 높은 가게로 orderby하고 순서대로 내어주기

# 지역별 리뷰어 랭킹 불러오기
@csrf_exempt
def callRankingReviewer(request):
    if request.method == "GET":

        # 랭킹을 보고자 하는 지역 -> 서버는 받아서 해당 지역 storeid를 검색해 테이블 구성 -> 해당 테이블에서 가장 많이 존재하는 userId -> username 출력
        rankingRegion = request.GET.get('rankingRegion')
        store_set = Store.objects.filter(region=rankingRegion)

        return HttpResponse(json.dumps({'result': 'testok'}))


# 지역별 가게 별점순 랭킹 불러오기
@csrf_exempt
def callRankingStore(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({'result': 'testok'}))