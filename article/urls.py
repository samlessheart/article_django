from django.urls import path
from . import views
from .views import  PostListView 
from .views import PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name="article-home"),
    path('about/', views.about, name="article-about"),
    path('contact/', views.contact, name= "article-contact"),
    path('search/', views.postsearchview, name= "article-search"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="article-Detail"),    

]
