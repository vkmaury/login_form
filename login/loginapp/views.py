from django.shortcuts import render, redirect
from .models import sign_up
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == "POST":
        login_em = request.POST['login_em']
        login_pass = request.POST['login_pass']
        if sign_up.objects.filter(email=login_em):
            data1 = sign_up.objects.filter(email=login_em).all()
            if sign_up.objects.filter(password=login_pass):
                request.session["em"] = login_em
                return redirect("profile")

            else:
                messages.error(request, 'Password Incorrect')
                return render(request, 'login.html')
        else:
            messages.error(request, 'Incorrect username plzz try again!!!')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        nm = request.POST['nm']
        em = request.POST['em']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 != pass2:
            messages.error(request, 'password Do not match')
            return redirect('customersignup')
        sign_up(name=nm, email=em, password=pass1).save()
        messages.success(request, 'Sign Up Successfully!!!')
        return redirect('login')
    else:
        return render(request, 'signup.html')




def profile(request):
    em = request.session.get("em")
    data1 = sign_up.objects.filter(email=em).all()
    return render(request, 'profile.html', {'data1': data1})
