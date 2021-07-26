from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import auth
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
@login_required
def Dashboard(request):
    return render(request, 'secret/index.html',{"user":request.user});

def Login(request):
    msg = ""
    if(request.method=="POST"):
        user = auth.authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            if user.is_superuser:
                auth.login(request, user)
                return redirect("/secret/")
            else:
                msg = "Login from Mobile App!"
        else:
            msg = "Incorrect Password!"
    print(msg)
    return render(request, 'secret/login.html',{"msg":msg});

def Register(request):
    return render(request, 'secret/register.html');

def ForgotPassword(request):
    return render(request, 'secret/forgot-password.html');

@login_required
def Settings(request):
    return render(request, 'secret/settings.html',{"msg":request.GET.get('q'),"err":request.GET.get('e')});

@login_required
def Profile(request):
    msg = ""
    if request.method=="POST":
        u = request.user
        u.first_name = request.POST.get('first_name')
        u.last_name  = request.POST.get('last_name')
        u.email      = request.POST.get('email')
        u.save()
        msg="Information Updated!"
    return redirect("/secret/settings/?q="+msg)

@login_required
def ChangePassword(request):
    msg = ""
    err = ""
    if request.method=="POST":
        u     = request.user
        opwd  = request.POST.get('opwd')
        npwd  = request.POST.get('npwd')
        cnpwd = request.POST.get('cnpwd')
        if u.check_password(opwd) == True:
            if npwd == cnpwd:
                u.set_password(npwd)
                msg="Password Updated!"
            else:
                err="New password(s) didn't match!"
        else:
            err="Incorrect Password!"
        u.save()
    return redirect("/secret/settings/?q="+msg+"&e="+err)

@login_required
def SampleListing(request):
    return render(request, 'secret/tables.html');

@login_required
def SampleReports(request):
    return render(request, 'secret/charts.html');
    
def NotFound(request):
    return render(request, 'secret/404.html');

@login_required
def Logout(request):
    auth.logout(request)
    return redirect('/secret/login/')


