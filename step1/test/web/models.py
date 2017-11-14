from django.db import models

# Create your models here.
class WebSite(models.Model):
    name=models.CharField(max_length=50)
    url=models.CharField(max_length=500)
    createTime=models.DateField(auto_now=True)

