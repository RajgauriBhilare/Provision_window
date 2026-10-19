from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from rest_framework import serializers

from .models import ContactEnquiry, Product, Project

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'date_joined', 'password']
        read_only_fields = ['id', 'date_joined', 'is_staff']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        user.set_password(password or get_random_string(32))
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save(update_fields=['password'])
        return user


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'description', 'image', 'created_at']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'location', 'category', 'description', 'image', 'created_at']


class ContactEnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactEnquiry
        fields = ['id', 'name', 'email', 'phone', 'subject', 'message', 'created_at']
