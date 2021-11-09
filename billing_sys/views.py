from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import User
from .forms import PostForm
from django.contrib import messages

# Create your views here.

def billing_sys(request):
    return render (request, ('index.html'))

def user_details(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Post Created')
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'user_details.html', {"form": form})

def bill(request):
    
    return render(request, ('bill.html'))
