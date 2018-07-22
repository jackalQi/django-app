from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.get_posts),
    path('<int: id>', views.get_post),
]