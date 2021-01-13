from django.db import models

class job(models.Model):
    image=models.ImageField(default="default.png",blank=True)
    sumamary=models.CharField(max_length=200)
  
