from rest_framework import serializers
from .models import UserProfile,ProfileFeedItem

class HelloSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=25)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields=('id','email','First_name','Last_name','password')
        extra_kwargs={
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }
    def create(self, validated_data):
        """create and return a new user"""
        user=UserProfile.objects.create_user(
            email=validated_data['email'],
            First_name=validated_data['First_name'],
            Last_name=validated_data['Last_name'],
            password=validated_data['password']
        )
        return user

class FeedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProfileFeedItem
        fields=('id','user_profile','status_text','created_on')
        extra_kwargs={
            'user_profile':{
                'read_only':True
            }
        }
