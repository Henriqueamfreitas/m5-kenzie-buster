from django.urls import path
from .views import MovieOrderView
from rest_framework_simplejwt import views

urlpatterns = [
    path('movies/<int:movie_id>/orders/', MovieOrderView.as_view()),
]    


