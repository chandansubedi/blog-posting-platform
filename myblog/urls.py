from django.urls import path 
from .import views
urlpatterns =[
    path('',views.ShowBlogs, name='ShowBlogs'),
    path('post_details/<int:pk>/', views.Post_details , name='post_details'),
    path('edit_post/<int:pk>/', views.edit_post , name='edit_post'),
    path('delete_post/<int:pk>/', views.Delete_post , name='delete_post'),
    path('search/', views.Search, name='search'),
]