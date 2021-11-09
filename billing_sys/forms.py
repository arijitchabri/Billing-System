from django.forms import ModelForm
from . models import User

class PostForm(ModelForm):
    class Meta:
        model = User
        field = '__all__'
        exclude = ('author',)