from django.db import models

# Create your models here.
class commerce(models.Model):

    productname=models.CharField(max_length=100)
    productprice=models.IntegerField()
    productimage=models.ImageField(upload_to='pics',null=True, blank=True)
    productdesc=models.TextField()
    large=models.BooleanField('large',default=False)
    medium=models.BooleanField('medium',default=False)
    small=models.BooleanField('small',default=False)

