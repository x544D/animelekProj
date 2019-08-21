from django.db import models

# Create your models here.

class Animes(models.Model):
    title = models.TextField()
    animePageLink = models.TextField()
    pageNum = models.IntegerField()
    coverLink = models.TextField()
    yearProd = models.IntegerField()
    rates = models.DecimalField(max_digits=10,decimal_places=1)
    types = models.TextField(null=True) #JSON-Serialied (TEXT)
    story = models.TextField()
