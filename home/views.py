from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import contact
from .forms import contactform
# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def info(request):
    return render(request, 'home/info.html')

def signup(request):
    if request.method=='POST':
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        username=request.POST['username']
        password1=request.POST['pass1']
        password2=request.POST['pass2']
        email=request.POST['email']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'username already exists')
            return redirect('/')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'email already exists')
            return redirect('/')
        elif password1!=password2:
            messages.error(request, 'passwords different')
            return redirect('/')
        else:
            user=User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
            user.save()
            messages.success(request, 'account created')
            return redirect('/')
    else:
        return render(request, 'home/signup.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['pass']

        user=auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'logged in successfully')
            return redirect('/')
        else:
            messages.error(request, 'invalid credentials')
            return redirect('/')
    else:
        return render(request, 'home/login.html')

def logout(request):
    auth.logout(request)
    messages.info(request, 'logged out successfully')
    return redirect('/')

    
def contact(request):
    if request.method=='POST':
        form=contactform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your query was submitted successfully')
        return redirect('/')
    else:
        form=contactform()
        return render(request, 'home/contact.html', {'form':form})