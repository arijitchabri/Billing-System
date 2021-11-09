from django.db import models

# Create your models here.

class Item(models.Model):
    dish = models.CharField(max_length= 100)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.id} {self.dish} {self.price}'

class User(models.Model):
    name = models.CharField(max_length=100, null = True, blank = True )
    ph_no = models.CharField(max_length= 10, null = True, blank = True )
    email = models.EmailField(null = True, blank = True )

    def __str__(self):
        return f'{self.id} {self.name}'