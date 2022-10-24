from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
import ticketSales
import accounts
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from accounts.forms import ProfileRegisterForm,ProfileEditForm,UserEditForm
from django.contrib.auth.models import User
from accounts.models import ProfileModel
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages



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



def profileRegisterView(request):

    if request.method=="POST":
        profileRegisterForm=ProfileRegisterForm(request.POST,request.FILES)
        if profileRegisterForm.is_valid():

            user = User.objects.create_user(username=profileRegisterForm.cleaned_data["username"],
                                email=profileRegisterForm.cleaned_data['email'],
                                password=profileRegisterForm.cleaned_data['password'],
                                first_name=profileRegisterForm.cleaned_data['first_name'],
                                last_name=profileRegisterForm.cleaned_data['last_name'])

            user.save()

            profileModel=ProfileModel(user=user,
                                       ProfileImage=profileRegisterForm.cleaned_data['ProfileImage'],
                                        Gender=profileRegisterForm.cleaned_data['Gender'],
                                        Credit=profileRegisterForm.cleaned_data['Credit'])

            profileModel.save()

            return HttpResponseRedirect(reverse(ticketSales.views.concertListView))
    else:
        profileRegisterForm=ProfileRegisterForm()

  
    context={
        "formData":profileRegisterForm
    }


    return render(request,"accounts/profileRegister.html",context)


def ProfileEditView(request):
    
    if request.method=="POST":
        profileEditForm=ProfileEditForm(request.POST,request.FILES, instance=request.user.profile)
        userEditForm=UserEditForm(request.POST,instance=request.user)
        if profileEditForm.is_valid and userEditForm.is_valid:
            profileEditForm.save()
            userEditForm.save()
            return HttpResponseRedirect(reverse(accounts.views.profileView))
    else:
        profileEditForm=ProfileEditForm(instance=request.user.profile)
        userEditForm=UserEditForm(instance=request.user)

    context={

        "profileEditForm":profileEditForm,
        "userEditForm":userEditForm,
        "ProfileImage":request.user.profile.ProfileImage,
        
    }

    return render(request,"accounts/profileEdit.html",context)
    
@login_required
def changePasswordView(request):
    
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/changepassword.html', {'form': form})