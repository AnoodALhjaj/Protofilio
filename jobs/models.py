from django.db import models

class job(models.Model):
    image=models.ImageField(upload_to='images')
    sumamary=models.CharField(max_length=200)
 
