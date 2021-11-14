from django import forms
from django.forms import ModelForm
from . models import New_user, Order

class PostForm(ModelForm):
    
    class Meta:
        model = New_user
        fields = ['name', 'email', 'ph_no']



# class Check(forms.Form):


class Order(ModelForm):

    class Meta:
        model = Order
        fields = ['chicken_65', 
        'chicken_hundi',
         'mutton_kosha',
          'biryani', 
          'keshar_lassi',
           'rosogolla',
            'butter_scotch',
             'special_rajasthani_thali',
              'ramen',
               'jeera_rice',
                'rainbow_mousse', 
                'paneer_pakora']


