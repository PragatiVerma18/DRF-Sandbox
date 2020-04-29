from django.conf.urls import url
from .views import (
    StatusAPIView,
    # StatusCreateAPIView, 
    # StatusDetailAPIView, 
    # StatusUpdateAPIView,
    # StatusDeleteAPIView
     )

urlpatterns = [
    url(r'^$', StatusAPIView.as_view()),                           # returns a list of data
    # url(r'^create/$', StatusCreateAPIView.as_view()),              # allows to create an instance
    # url(r'^(?P<pk>\d+)/$', StatusDetailAPIView.as_view()),         # allows to get details of any specific instance
    # url(r'^(?P<pk>\d+)/update/$', StatusUpdateAPIView.as_view()),  # allows to update a specific instance
    # url(r'^(?P<pk>\d+)/delete/$', StatusDeleteAPIView.as_view()),  # allows to delete a specific instance
]
