from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import generics, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import JsonResponse
import requests
import json
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import exception_handler
from .serializers import AzaSerializer
import environ
env = environ.Env()
environ.Env.read_env() 


# Create your views here.
# class Getaza(generics.CreateAPIView):
#     serializer_class = AzaSerializer
#     def getAza(request):
#        serializer_class = AzaSerializer(data=request.data)
#        aza_num = serializer_class.data['number']
#        aza_code = serializer_class.data['code']

#        headers = {
#            'Authorization': 'Bearer sk_test_37a1a4de8362acf2c2037889c8b440f7da559787',
#        }
#        # # params = {
#        # #     '3112000854': 'account_number',
#        # #     '011': 'bank_code'
#        # # }
#        # account_number = '2408264600'
#        # bank_code = '057'
#        response = requests.get('https://api.paystack.co/bank/resolve?account_number='+aza_num+'&bank_code='+aza_code, headers=headers)
#        result = response.content
#        data = json.loads(response.text)
       
#        account_name = data.get("data").get("account_name")
#        account_name = serializer_class.data['name']
#        return HttpResponse(account_name)
       # if serializer.is_valid():
       #     serializer.save()
       # return Response(serializer.data)

class Verify(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request, number, code):
        number = number
        code = code

        headers = {
            'Authorization': env('Bearer'),
        }

        # # params = {
        # #     '3112000854': 'account_number',
        # #     '011': 'bank_code'
        # # }

        # account_number = '2408264600'
        # bank_code = '057'

        
        response = requests.get('https://api.paystack.co/bank/resolve?account_number='+number+'&bank_code='+code, headers=headers)
        result = response.content
        data = json.loads(response.text)

        # account_name = data.get("data").get("account_name")
        # response = exception_handler(number, code)
        # if response is not None:
        #     response.data['Failure'] = 'Not Found'
        return JsonResponse(data)   
        

        # print(x)
        # y = x.lower()
        # print(y)
