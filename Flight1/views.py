from django.shortcuts import render
from django.http import HttpResponse,  HttpResponseRedirect
from django.views import View
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView
from .forms import PasswordChangingForm
from .models import *
# Create your views here.


def index(request):
    return render(request,'Flight1/Home.html')

class LoginClass(View):
    def get(self,request):
         return render(request,'Flight1/login.html')
    
    def post(self,request):
        user_name =request.POST.get('tendangnhap')
        pass_word= request.POST.get('matkhau')
        my_user = authenticate(username=user_name,password=pass_word)
        if my_user is None:
             return render(request, "Flight1/login.html", {
                "message": "Invalid username and/or password."
            })
        login(request, my_user)
        return HttpResponseRedirect(reverse("Flight1:index"))

class RegisterClass(View):
    def get(self,request):
         return render(request,'Flight1/register.html')    
    
    def post(self,request):
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        IDcode = request.POST['identification']
       

        # Kiem tra mk trung khop
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "Flight1/register.html", {
                "message": "Passwords must match."
            })
        # Tao user moi
        else:
            try:
                new_user = User.objects.create_user(username, email, password)
                new_user.first_name = fname
                new_user.last_name = lname
                new_user.ID_code = IDcode
                new_user.phone_number = phone
                new_user.save()
            except:
                return render(request, "Flight1/register.html", {
                    "message": "Username already taken."
                })
            
            return render(request, "Flight1/register.html",{
                    "message": "Register successfully"})

class PasswordChangeClass (PasswordChangeView):
       form_class = PasswordChangingForm
       success_url = reverse_lazy('Flight1:index')
    
      
       
def logoutdef(request):
    logout(request)
    return HttpResponseRedirect(reverse("Flight1:index"))