from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import signUpForm

# all about signup function 
def sign_up(request):
    if request.method =='POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ShowBlogs')
    else:
        form = signUpForm ()
    context = {
        'form':form,
    }
    return render(request,'Accounts/signup.html',context)

def userProfile(request):
    return render(request, 'accounts/usersProfile.html')