from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Update
from django.views.generic import View
from restapi.mixins import JsonResponseMixin
from django.core.serializers import serialize
import json

def update_model_detail_view(request):
  data = {
    "hello": "pragati",
    "id": 1,
  }
  return JsonResponse(data)

class JsonCBV(View):
  def get(self, request, *args, **kwargs):
    data = {
    "hello": "pragati",
    "id": 1,
    }
    return JsonResponse(data)

class JsonCBV2(JsonResponseMixin, View):
  def get(self, request, *args, **kwargs):
    data = {
      "count": 1000,
      "content": "some new content"
    }
    return self.render_to_json_response(data)

class SerializedDetailView(View):
  def get(self, request, *args, **kwargs):
    obj = Update.objects.get(id=1)
    json_data=obj.serialize()
    return HttpResponse(json_data, content_type='application/json')

class SerializedListView(View):
  def get(self, request, *args, **kwargs):
    qs = Update.objects.all()
    # data = serialize("json", qs, fields=('user', 'content'))
    json_data = Update.objects.all().serialize()
    return HttpResponse(json_data, content_type='application/json')