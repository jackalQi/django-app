from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.get_posts, name='posts_list'),
    path('post/<int:pk>/', views.get_post, name='post_detail'),

]
