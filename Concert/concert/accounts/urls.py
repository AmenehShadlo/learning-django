from django.urls import path
from accounts import views


urlpatterns = [
    path('login/', views.loginView,name="login"),
    path('logout/', views.logoutView),
]