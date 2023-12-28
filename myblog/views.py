
import requests
# import keras
# from keras.models import load_model
# from keras.utils import pad_sequences
from django.db.models import Count
# from nltk.tokenize import word_tokenize
# from nltk.stem import WordNetLemmatizer
# from nltk.corpus import stopwords
# import nltk
# import pickle
import os
from django.conf import settings

from django.views.decorators.csrf import csrf_exempt
# import pickle
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# import numpy as np

# importing things 

# import joblib
from django.shortcuts import render, redirect
from .models import BlogModel 
from .forms import BlogModelForm,BlogUpdateForm ,CommentForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# model_path = 'datas/model.pkl'
# model = joblib.load(model_path)

# def preprocess_input(text_content, tokenizer, max_sequence_length):
#     sequences = tokenizer.texts_to_sequences([text_content])
#     padded_sequences = pad_sequences(sequences, maxlen=max_sequence_length)
#     return np.array(padded_sequences)
# with open('modelFile/model.pkl', 'rb') as file:
#     model = pickle.load(file)

# max_len = 100  # Assuming a maximum sequence length of 100 (adjust as needed)
# tokenizer = Tokenizer()    

# # Instantiate the Tokenizer
# tokenizer = Tokenizer()
# max_len = 1000

from datetime import datetime
import pytz
# Create your views here.


def convert_fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) * 5.0/9.0)

def ShowBlogs(request):
    # model_path = 'modelFile/model.pkl'
    # model = joblib.load(model_path)
    
    postsM = BlogModel.objects.order_by('-date_created')[:5]
    posts = BlogModel.objects.all()
    page = Paginator(posts,3)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    
    if request.method == 'POST':
        form = BlogModelForm(request.POST)
        if form.is_valid():
            # text = [form.cleaned_data['content']]
            # sequences = tokenizer.texts_to_sequences([text])
            # padded_sequence = pad_sequences(sequences, maxlen=max_len)
            # prediction = model.predict(np.array(padded_sequence))

            # Assuming binary classification, adjust as needed for your case
            # result = "Positive" if prediction > 0.5 else "Negative"
            # print(result)



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
            # prediction = model.predict(np.array(padded_sequence))

            # new change 
            # cleaned_text = remove_stop_words(text)
            # sequence = tokenizer.texts_to_sequences([cleaned_text])
            # padded_sequence = pad_sequences(sequence, maxlen=1250)
            # prediction = model_lstm.predict(padded_sequence)[0][0]
            

            instance = form.save(commit=False)
            instance.author = request.user
            # instance.accuracy = result 

            # instance.predicted_class = predicted_class  # Add a field to your BlogModel to store predictions
            instance.save()
            return redirect('ShowBlogs') 
    else:
        form = BlogModelForm()

     # Fetch most commented posts
    most_commented_posts = BlogModel.objects.annotate(comment_count=Count('postcomments')).order_by('-comment_count')[:4]
    sportTitle = BlogModel.objects.filter(category='sport').order_by('-date_created')[:3]
    # weather 
    api_key = '8e9f2c1f4bd1916f31aceea38384cb28'
    city_name = 'Pokhara'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=imperial&appid={api_key}'
    response = requests.get(url)
    response.raise_for_status()
    weather_data = response.json()
    temperature_fahrenheit = weather_data['main']['temp']
    temperature_celsius = convert_fahrenheit_to_celsius(temperature_fahrenheit)




    # weather 
    # date 
    current_datetime_utc = datetime.utcnow()

    kathmandu_timezone = pytz.timezone('Asia/Kathmandu')
    current_datetime_ktm = current_datetime_utc.replace(tzinfo=pytz.utc).astimezone(kathmandu_timezone)

    # date 




    context = {
        'page':page,
        'form':form,
        'postsM':postsM,
        'most_commented_posts': most_commented_posts,
        'sportTitle':sportTitle,
        'city': weather_data['name'],
        'temperature': temperature_celsius,
        'description': weather_data['weather'][0]['description'],
        'icon': weather_data['weather'][0]['icon'],
        'current_datetime_ktm': current_datetime_ktm,

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
def Post_category_sport(request):
    post = BlogModel.objects.filter(category='sport')
    context = {           
        'post':post
    }
    return render(request,'blogs/post_category_sport.html',context)

def Post_category_politics(request):
    post = BlogModel.objects.filter(category='politics')
    context = {           
        'post':post
    }
    return render(request,'blogs/post_category_politics.html',context)

def Post_category_weather(request):
    post = BlogModel.objects.filter(category='weather')
    context = {           
        'post':post
    }
    return render(request,'blogs/post_category_weather.html',context)

def Post_category_health(request):
    post = BlogModel.objects.filter(category='health')
    context = {           
        'post':post
    }
    return render(request,'blogs/post_category_health.html',context)




