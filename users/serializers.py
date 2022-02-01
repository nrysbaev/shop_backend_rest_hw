from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User


class UserValidateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()

    def validate_username(self, username):
        user = User.objects.filter(username=username)
        if user:
            raise ValidationError('This username is already taken!')
        return username

    def validate_email(self, email):
        user = User.objects.filter(email=email)
        if user:
            raise ValidationError('This email already exists!')
        return email
