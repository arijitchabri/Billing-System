from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . import models
from .forms import PostForm, Order
from django.contrib import messages

# Create your views here.


def billing_sys(request):
    if request.method == 'POST':
        form = Order(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'user_details.html')
    else:
        form = Order()
    return render (request, ('index.html'))

def user_details(request):

    id_list = models.Order.objects.values('id')
    id_list_2 = []
    for i in id_list:
        id_list_2.append(i['id'])
    max_id = max(id_list_2)
    print('id_list : ', max_id)

    order_list = models.Order.objects.filter(id = max_id)

    print('order_list : ' , order_list)
    order_str = ""
    for i in order_list:
        order_str = i
        order_str = str(order_str)
        order_str = order_str.split(", ")
    print(order_str)

    j = 0
    final_order_id = []

    total = 0

    price_data_store = []

    for i in order_str:
        j = j+1
        if i == "True":
            final_order_id.append(j)
            price_data = models.Item.objects.filter(id = j).values('price')
            price_data_store.append(price_data)

    print("price data store: ")
    for i in price_data_store:
        for j in i:
            total = total + j['price']

    


    print("final order id : " , final_order_id)

    ordered_item_data = []

    for i in final_order_id:
        
        ordered_item_data.append(models.Item.objects.filter(id = i))

    print("Final data : ", ordered_item_data)



    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            if form:

                form.save()
                name = form.cleaned_data['name'] 
                print(name)
                context = {'name': name,
                        'data' : ordered_item_data,
                        'total' : total
                    }
                #messages.success(request, f'User Created')
                return render(request, ('bill.html'), context = context)
            else:
                return render(request, 'user_details.html')
    else:
        form = PostForm()
    return render(request, 'user_details.html', {"form": form})



    