from django.db import models

class products(models.Model):
    pid = models.AutoField(primary_key=True)
    pname=models.CharField(max_length=50)
    pimg=models.ImageField(upload_to="myimage",null=True)
    pprice=models.IntegerField()



class product(models.Model):
    # pid = models.AutoField(primary_key=True)
    pname=models.CharField(max_length=50)
    pimg=models.ImageField(upload_to="myimage",null=True)
    pprice=models.IntegerField()