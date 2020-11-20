from django.urls import path
from .           import views

urlpatterns = [
    path(''          , views.homePageView, name='homePageView'),
    path('verifyfreq', views.verifyfreq  , name='verifyfreq'),
]
