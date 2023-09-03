from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.


def signin(request):
    if 'username' in request.session:
        return redirect(main)
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            request.session['username'] = username
            return redirect('main')
        else:
            messages.error(request,"invalid login")
            return redirect('signin')
    else:
            # User is authenticated
        return render(request,"login.html")


def main(request):
    username = ''
    if 'username' in request.session:
        username = request.session['username'] 
        return render(request, 'main.html',{'username':username})
    return redirect(signin)


def signup(request):
    if 'username' in request.session:
        return redirect('main')
    if request.method == "POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request,"username already exists")
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.error(request,"email taken")  
            return redirect('signup')
        elif len(password) < 6: 
            messages.error(request, "Password must be at least 6 characters long")
            return redirect('signup')
        else:  
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save()
            messages.info(request,"User Created successfully")
            return redirect('signin')
    else:
        return render(request,"signup.html")

def logout(request):
    if 'username' in request.session:
        request.session.flush()  # Clear the session
    return redirect('signin')  # Change 'login' to the URL name of your login page
