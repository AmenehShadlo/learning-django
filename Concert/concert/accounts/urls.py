from django.urls import path
from accounts import views


urlpatterns = [
    path('login/', views.loginView,name="login"),
    path('logout/', views.logoutView),
    path('profile/', views.profileView),
    path('profileRegister', views.profileRegisterView),
    path('profileEdit', views.ProfileEditView),
    path('changepassword',views.changePasswordView,name='change_password'),

]