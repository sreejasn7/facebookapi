__author__ = ""
__copyright__ = ""
__maintainer__ = ""
__version__ = ""

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


class FacebookLabelRelatedSerializer(serializers.ModelSerializer):
    access_token = serializers.ReadOnlyField(source='page.access_token', read_only=True)
    user = serializers.ReadOnlyField(source='owner.ps_id', read_only=True)

    class Meta:
        model = FacebookLabel
        fields = ('owner', 'page', 'label_id', 'access_token', 'user',)