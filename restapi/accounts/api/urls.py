from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from updates.views import(
    update_model_detail_view,
    JsonCBV,
    JsonCBV2,
    SerializedListView,
    SerializedDetailView
    )

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import AuthAPIView, RegisterAPIView
app_name = 'accounts.api'
urlpatterns = [

    url(r'^$', AuthAPIView.as_view()),
    url(r'^register/$', RegisterAPIView.as_view()),

    url(r'^jwt/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    url(r'^jwt/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),


] 

