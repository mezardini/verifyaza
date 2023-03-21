from django.contrib import admin
from django.urls import path
from . import views
from .views import Verify

urlpatterns = [
    path("verify/<str:number>/<str:code>", Verify.as_view(), name="verify"),
    # path('verifyname', Getaza.as_view(), name='aza')
    
]