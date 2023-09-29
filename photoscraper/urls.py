from django.urls import path
from .views import *

urlpatterns = [
    path('api/scrape/', ScrapedPhotoView.as_view(), name='scrape-data'),
]
