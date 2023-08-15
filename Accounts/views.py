from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import signUpForm , AccountUpdateForm , UserUpdateForm

# all about signup function 
def sign_up(request):
    if request.method =='POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = signUpForm ()
    context = {
        'form':form,
    }
    return render(request,'Accounts/signup.html',context)

# edit profile of user (change details)
def userProfile(request):
    if request.method =='POST':
        u_form = UserUpdateForm(request.POST or None ,instance=request.user )
        p_form = AccountUpdateForm(request.POST or None , request.FILES or None,instance=request.user.accountmodel )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('userProfile')
    else:
        u_form = UserUpdateForm(instance = request.user )
        p_form = AccountUpdateForm(instance= request.user.accountmodel)
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'accounts/usersProfile.html',context)