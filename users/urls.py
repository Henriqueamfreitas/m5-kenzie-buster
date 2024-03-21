from django.urls import path
from users.views import UserView, LoginJWTView, UserDetailView
from rest_framework_simplejwt import views

urlpatterns = [
    path('users/', UserView.as_view()),
    path('users/login/', LoginJWTView.as_view()),
    path('users/login/refresh/', views.TokenRefreshView.as_view()),
    path('users/<int:user_id>/', UserDetailView.as_view()),
]    


