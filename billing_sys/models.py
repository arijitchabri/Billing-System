from django.db import models

# Create your models here.

class Item(models.Model):
    dish = models.CharField(max_length= 100)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.id} {self.dish} {self.price}'

class New_user(models.Model):
    name = models.CharField(max_length=100)
    ph_no = models.CharField(max_length= 10)
    email = models.EmailField()

    def __str__(self):
        return f'{self.id }, "   ", { self.name}'

class Order(models.Model):

    chicken_65 = models.BooleanField()
    paneer_pakora = models.BooleanField()

    biryani = models.BooleanField()
    chicken_hundi = models.BooleanField()
    jeera_rice = models.BooleanField()
    mutton_kosha = models.BooleanField()
    special_rajasthani_thali = models.BooleanField()
    ramen = models.BooleanField()

    rosogolla = models.BooleanField()
    keshar_lassi = models.BooleanField()
    butter_scotch = models.BooleanField()
    rainbow_mousse = models.BooleanField()

    def __str__(self):
        return f'{self.chicken_65}, {self.paneer_pakora}, {self.biryani}, {self.chicken_hundi}, {self.jeera_rice}, {self.mutton_kosha}, {self.special_rajasthani_thali}, {self.ramen}, {self.rosogolla}, {self.keshar_lassi}, {self.butter_scotch}, {self.rainbow_mousse}'



