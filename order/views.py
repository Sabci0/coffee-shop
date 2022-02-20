from django.shortcuts import render, redirect

from order.forms import UserForm


def order_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home:home')
    else:
        form = UserForm()

    return render(request,'order/order.html',{'form':form})
