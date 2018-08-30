# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
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
    if request.method == "POST":
        return HttpResponse(json.dumps({'result': 'testok'}))


# 지역별 가게 별점순 랭킹 불러오기
@csrf_exempt
def callRankingStore(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({'result': 'testok'}))