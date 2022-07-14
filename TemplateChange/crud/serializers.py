from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import Profile,Address

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = Profile
        fields = '__all__'

class AddressSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"
