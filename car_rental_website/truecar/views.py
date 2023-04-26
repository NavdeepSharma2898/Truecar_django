from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Product, Hatchback, Sedan, Suv, Allcars
from math import ceil
from django.contrib.auth  import authenticate,  login, logout
# Create your views here.


def index(request):
    products = Product.objects.all()

    # LOGIC FOR NUMBER OF SLIDES TO BE DISPLAYED
    n = len(products)
    nslides = n//3 + ceil((n/3)-(n//3))
    params = {'no_of_slides': nslides, 'product': products, 'range': range(1, nslides)}
    return render(request, 'truecar/index.html', params)

def about(request):
    return render(request, 'truecar/about.html')

def handeLogin(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("handleLogin")

    return render(request, 'truecar/login.html')

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('handleLogin')


def registration(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        address = request.POST.get('address', '')
        cpassword = request.POST.get('cpassword', '')

        # check for errorneous input
        if (password != cpassword):
            messages.error(request, " Passwords do not match")
            return redirect('registration')
        # Create the user

        myuser = User.objects.create_user(name, email, password)
        myuser.phone = phone
        myuser.address = address
        myuser.save()
        messages.success(request, " Your Account has been successfully created")
        return redirect('handleLogin')
    return render(request, 'truecar/registration.html')

def searchMatch(query, item):
    '''return true only if query matches the item'''
    if query in item.desc or query in item.product_name or query in item.category:
        return True
    else:
        return False

def search(request):
    allcars = Allcars.objects.all()
    query = request.GET.get('search', '')
    test1 = [item for item in allcars if searchMatch(query, item)]
    params = {'test1': test1}

    return render(request, 'truecar/search.html', params)



def productview(request):
    return HttpResponse('WE ARE AT product view')

def checkout(request):
    return HttpResponse('WE ARE AT checkout')

def bookings(request):
    return render(request, 'truecar/bookings.html')

def suv(request):

     suv = Suv.objects.all()
     params = {'suv': suv}
     return render(request, "truecar/suv.html", params)

def sedan(request):
    sedan = Sedan.objects.all()
    params = {'sedan': sedan}
    return render(request, "truecar/sedan.html", params)

def hatchback(request):
    hatchback = Hatchback.objects.all()
    params = {'hatchback': hatchback}
    return render(request, "truecar/hatchback.html", params)

