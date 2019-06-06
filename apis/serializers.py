from rest_framework import serializers
from .models import MessengerUser,FacebookLabel,FacebookPage


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessengerUser
        fields = ('ps_id',)


class FacebookLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacebookLabel
        fields = ('owner', 'page',)