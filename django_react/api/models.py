from django.db import models

# Create your models here.
class Article(models.Model):
    title =  models.CharField(max_length=100)
    description = models.CharField(max_length=5000)


    def __str__(self):
         return self.title




