from rest_framework import serializers
from status.models import Status
# from accounts.api.users.serializers import UserPublicSerializer
from rest_framework.reverse import reverse as api_reverse
class CustomSerializer(serializers.Serializer):
  content = serializers.CharField()
  email = serializers.EmailField()

class StatusInlineUserSerializer(serializers.ModelSerializer):
  uri = serializers.SerializerMethodField(read_only= True)
  class Meta:
    model = Status
    fields = [
      'uri',
      'id',
      'content',
      'image'
    ]

  def get_uri(self, obj):
    request = self.context.get('request')
    # return "/api/status/{id}/".format(id=obj.id)
    return api_reverse('api-status:detail', kwargs={"id":obj.id}, request=request)



class StatusSerializer(serializers.ModelSerializer):
  uri = serializers.SerializerMethodField(read_only= True)
  # user = UserPublicSerializer(read_only=True)
  class Meta:
    model = Status
    fields = [
      'uri',
      'id',
      # 'user',
      'content',
      'image'
    ]
    # read_only_fields = ['user']

  def get_uri(self, obj):
    return "/api/status/{id}/".format(id=obj.id)

    
  def validate_content(self, value):
    if len(value)>10000:
      raise serializers.ValidationError("This is wayy too long.")
    return value
  
  def validate(self, data):
    content = data.get("content", None)
    if content =="":
      content = None
    image = data.get("image", None)
    if content is None and image is None:
      raise serializers.ValidationError("content or image is required.")
    return data