from django.db import models

# Models is created to show the producs details which is needed to show like like photos

class Product(models.Model):
    Title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='media/productImage/')
    about = models.TextField(max_length=1000)
