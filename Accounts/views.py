from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def sign_up(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ShowBlogs')
    else:
        form = UserCreationForm()
    context = {
        'form':form,
    }
    return render(request,'Accounts/signup.html',context)