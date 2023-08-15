from django.shortcuts import render, redirect
from .models import BlogModel
from .forms import BlogModelForm,BlogUpdateForm 

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



def Post_details(request,pk):
    post=BlogModel.objects.get(id=pk)
    context ={
        'post':post
    }
    return render(request,'blogs/post_details.html',context)


def edit_post(request, pk):
    post= BlogModel.objects.get(id=pk)
    if request.method == 'POST':
        form = BlogUpdateForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_details',pk=post.id)
    else:
        form = BlogUpdateForm(instance=post)    
    context={
        'post':post,
        'form':form
    }
    return render(request,'blogs/edit_post.html',context)


def Delete_post(request , pk):
    post = BlogModel.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('ShowBlogs')
    context = {
        'post':post
    }
    return render(request,'blogs/delete_post.html',context)