from rest_framework import serializers
from Profile.models import Profile

from drf_dynamic_fields import DynamicFieldsMixin

class ProfileSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','user', 'address')
