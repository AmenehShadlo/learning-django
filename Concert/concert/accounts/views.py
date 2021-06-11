from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import ticketSales
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from accounts.forms import ProfileForm


def loginView(request):
    #Post
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET.get("next"))
                
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        else:
            context={
                "username":username,
                "errorMessage":"کاربری با این مشخصات یافت نشد"
            }
            return render(request, "accounts/login.html",context)
     #Get
    else:
        return render(request, "accounts/login.html",{})

def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse(ticketSales.views.concertListView))

@login_required
def profileView(request):
    profile=request.user.profile

    context={
        "profile":profile
    }

    return render(request,"accounts/profile.html",context)

@login_required
def profileEditView(request):
    profileForm=ProfileForm(instance=request.user.profile)

    context={
        "formData":profileForm
    }

    return render(request,"accounts/profileEdit.html",context)


