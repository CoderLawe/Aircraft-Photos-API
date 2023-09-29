from rest_framework import serializers
from .models import PhotoModel

# Create a model serializer
class PhotosSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = PhotoModel
        fields = ('image', 'copyright')