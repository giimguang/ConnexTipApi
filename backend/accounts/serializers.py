from rest_framework import serializers
from accounts.models import User

class accountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "password", "email")