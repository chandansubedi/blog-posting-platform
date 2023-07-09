from django.urls import path 
from .import views
urlpatterns =[
    path('',views.ShowBlogs, name='ShowBlogs')

]