from django.shortcuts import render ,HttpResponse , redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
     print(request.user)
     if request.user.is_anonymous:
         return redirect('/login')
     return render(request , 'index.html')

def loginuser(request):
    if request.method == 'POST':
        #  CHECK USER CREDTINAL IS IT TRUE OR NOT
        username= request.POST.get('username')
        password= request.POST.get('password')
        print(username , password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request , user)
    # A backend authenticated the credentials
            return redirect('/')
        else:
            return render(request , 'login.html')
    # No backend authenticated the credentials
    
    return render(request , 'login.html')

def logoutuser(request):
     logout(request)
     return redirect('/login')