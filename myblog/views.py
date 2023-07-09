from django.shortcuts import render, redirect
from .models import BlogModel
from .forms import BlogModelForm

# Create your views here.
def ShowBlogs(request):
    posts = BlogModel.objects.all()
    if request.method == 'POST':
        form =  BlogModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save() 
            return redirect('ShowBlogs')
    else:
        form =  BlogModelForm()


    context = {
        'posts':posts,
        'form':form
    }



    return render(request ,'blogs/index.html' , context) 