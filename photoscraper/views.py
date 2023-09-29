from django.shortcuts import render
# import viewsets
from rest_framework import viewsets

# import local data
from .serializers import PhotosSerializer
from .models import PhotoModel
from rest_framework import generics, status
from rest_framework.response import Response
# create a viewset

# Web scraping imports

from bs4 import BeautifulSoup
import requests
import lxml


class ScrapedPhotoView(generics.RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        # Perform web scraping using BeautifulSoup4
        # Extract the data you need

        reg = self.request.GET.get('inputParam', None)

        if reg is None:
            reg = "TG462"
        source = requests.get(
            f'https://www.jetphotos.com/photo/keyword/{reg}').text
        soup = BeautifulSoup(source, 'lxml')

        image = soup.find("img", class_="result__photo")['src']
        copyrightSpan = soup.find("span", class_="result__infoListText")
        copyright = copyrightSpan.find("a", class_="link").text

        print("image", image)
        print("copyright", copyright)

        scraped_data = {
            'image': image,
            'copyright': copyright,
        }

        serializer = PhotosSerializer(data=scraped_data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
# Create your views here.
