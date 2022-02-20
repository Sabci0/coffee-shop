from django.contrib.auth import login
from django.shortcuts import render, redirect

from order.forms import UserForm, UserDetail


def order_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user= form.save()
            login(request, user)
            return redirect('order:create_order_detail')
    else:
        form = UserForm()

    return render(request,'order/order.html',{'form':form })

def order_detail_view(request):
    if request.method =='POST':
        form = UserDetail(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home:home')
    else:
        form = UserDetail(initial={
            'username':request.user.username,
            'email':request.user.email

        })


    return render(request,'order/order_detail.html',{'form':form})



