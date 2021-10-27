from django.db import models

# Create your models here.
class Destination(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField(default=0)
    desc = models.TextField()
    offers = models.BooleanField(default=False)


