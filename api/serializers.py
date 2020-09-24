from rest_framework import serializers

from .models import Category, Profile

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    
    # category = CategorySerializer(required=True)
    # picture_url = serializers.SerializerMethodField('get_image_url')
    # email = serializers.EmailField(read_only=True)

    class Meta:
        model = Profile
        fields = ('category', 'breakfast', 'lunch','dinner','hour','rating')
    
    # def get_image_url(self, Profile):
    #     return Profile.picture.url