from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='Flight1'
urlpatterns = [
    path("",views.index, name='index'),
    path("login/",views.LoginClass.as_view(), name='login'),
    path("register/",views.RegisterClass.as_view(), name='register'),
    path("logout/",views.logoutdef, name='logout'),
    path("passwordchange", views.PasswordChangeClass.as_view(template_name='Flight1/passwordchange.html'), name='passchange')
    
]