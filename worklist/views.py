from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from worklist.models import *
from worklist.serializers import *
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


@api_view(['GET'])
def wl_detail(request):
    if request.method == 'GET':
        user = request.GET.get('user', None)
        if user is not None:
            accounts = CaseDetail.objects.filter(STAFF_ID=user)
            accounts_serializer = CaseDetailSerializer(accounts, many=True)
        else:
            return JsonResponse("user must fill", safe=False)

        return JsonResponse(accounts_serializer.data, safe=False)

@api_view(['GET'])
def wl_summary_total(request):
    if request.method == 'GET':
        user = request.GET.get('user', None)
        
        if user is not None:
            items = TotalView.objects.filter(STAFF_ID=user)
            items_serializer = TotalViewSerializer(items, many=True)
        else:
            return JsonResponse("user must fill", safe=False)

        return JsonResponse(items_serializer.data, safe=False)


        