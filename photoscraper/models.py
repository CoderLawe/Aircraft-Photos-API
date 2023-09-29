from django.db import models

# Create your models here.


class PhotoModel(models.Model):
    image = models.CharField(max_length=1000)
    copyright = models.CharField(max_length=200)

    def __str__(self):
        return self.image
