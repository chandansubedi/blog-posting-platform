import keras
from keras.models import load_model
from keras.utils import pad_sequences
# from nltk.tokenize import word_tokenize
# from nltk.stem import WordNetLemmatizer
# from nltk.corpus import stopwords
# import nltk
# import pickle
import os
from django.conf import settings

from django.views.decorators.csrf import csrf_exempt
import pickle
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# importing things 

import joblib
from django.shortcuts import render, redirect
from .models import BlogModel
from .forms import BlogModelForm,BlogUpdateForm ,CommentForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
# model_path = 'datas/model.pkl'
# model = joblib.load(model_path)

# def preprocess_input(text_content, tokenizer, max_sequence_length):
#     sequences = tokenizer.texts_to_sequences([text_content])
#     padded_sequences = pad_sequences(sequences, maxlen=max_sequence_length)
#     return np.array(padded_sequences)
with open('modelFile/model.pkl', 'rb') as file:
    model = pickle.load(file)

max_len = 100  # Assuming a maximum sequence length of 100 (adjust as needed)
tokenizer = Tokenizer()    

# # Instantiate the Tokenizer
# tokenizer = Tokenizer()
# max_len = 1000

# Create your views here.
def ShowBlogs(request):
    model_path = 'modelFile/model.pkl'
    model = joblib.load(model_path)
    
    postsM = BlogModel.objects.order_by('-date_created')[:5]
    posts = BlogModel.objects.all()
    page = Paginator(posts,3)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    if request.method == 'POST':
        form = BlogModelForm(request.POST)
        if form.is_valid():
            text = [form.cleaned_data['content']]
            sequences = tokenizer.texts_to_sequences([text])
            padded_sequence = pad_sequences(sequences, maxlen=max_len)
            prediction = model.predict(np.array(padded_sequence))

            # Assuming binary classification, adjust as needed for your case
            result = "Positive" if prediction > 0.5 else "Negative"
            print(result)


            # text = request.POST.get('content', '')

            # Tokenize and pad the input text
            # sequences = tokenizer.texts_to_sequences(text_content)
            # # padded_sequences = pad_sequences(sequences, maxlen=max_len, padding='post')
            # padded_sequence = pad_sequences(sequence, maxlen=1250)

            # # Make predictions
            # prediction = model.predict(padded_sequences)[0][0]

            # # Assuming binary classification, you can threshold the prediction
            # threshold = 0.5
            # predicted_class = 1 if prediction > threshold else 0

            # new change 
            # cleaned_text = remove_stop_words(text)
            # sequence = tokenizer.texts_to_sequences([cleaned_text])
            # padded_sequence = pad_sequences(sequence, maxlen=1250)
            # prediction = model_lstm.predict(padded_sequence)[0][0]
            

            instance = form.save(commit=False)
            instance.author = request.user
            # instance.predicted_class = predicted_class  # Add a field to your BlogModel to store predictions
            instance.save()
            return redirect('ShowBlogs') 
    else:
        form = BlogModelForm()
    context = {
        'page':page,
        'form':form,
        'postsM':postsM
    }
    return render(request ,'blogs/index.html' , context) 

def MarqueeNdetails(request,pk):
    return render(request,'blogs/post_details.html')

def Post_details(request,pk):
    post = BlogModel.objects.get(id=pk)
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            isinstance = c_form.save(commit=False)
            isinstance.user = request.user
            isinstance.post = post  
            isinstance.save()
            return redirect('post_details',pk=post.id)
    else:
        c_form = CommentForm()    
    post=BlogModel.objects.get(id=pk)
    context ={
        'post':post,
        'c_form':c_form 
    } 
    return render(request,'blogs/post_details.html',context)

@login_required
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

@login_required
def Delete_post(request , pk):
    post = BlogModel.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('ShowBlogs')
    context = {
        'post':post
    }
    return render(request,'blogs/delete_post.html',context)



def Search(request):
    query = request.GET['search']
    posts = BlogModel.objects.filter(title__icontains=query)
    context = {
        'posts':posts
    }
    return render(request,'blogs/search.html',context)

# def MarqueeNews(request):
#     postsM = BlogModel.objects.filter('-created_at')[:5]
#     context = {
#         'postsM':postsM
#     }
#     return render(request ,'blogs/index.html' , context)
 