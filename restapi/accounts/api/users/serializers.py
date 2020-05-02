from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import serializers
from status.api.serializers import StatusInlineUserSerializer

User = get_user_model()



# nested serializer
class UserPublicSerializer(serializers.ModelSerializer):
  uri = serializers.SerializerMethodField(read_only=True)
  # status_list = serializers.SerializerMethodField(read_only=True)
  status = serializers.SerializerMethodField(read_only = True)
  class Meta:
    model = User
    fields = [
      'id',
      'username',
      'uri',
      # 'status_list',
      'status',
    ]  

  def get_uri(self, obj):
    return "/api/users/{id}/".format(id=obj.id)

  # def get_status_list(self, obj):
  #   qs = obj.status_set.all()
  #   return StatusInlineUserSerializer(qs, many=True).data

  def get_status(self, obj):
    request = self.context.get('request')
    limit= 4
    if request:
      limit_query = request.GET.get('limit')
      try:
        limit = int(limit_query)
      except:
        pass
    qs = obj.status_set.all().order_by("-timestamp")
    data = {
      'uri': self.get_uri(obj)+"status/",
      'last': StatusInlineUserSerializer(qs.first()).data,
      'recent': StatusInlineUserSerializer(qs[:limit], many=True).data
    }
    return data

## To test the limiting stuff see: http://127.0.0.1:8000/api/user/pragati/?limit=3