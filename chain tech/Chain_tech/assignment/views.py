from django.shortcuts import render
import datetime
import random
from django.shortcuts import HttpResponse
from .models import *

# Create your views here.
def home(request):
    now = datetime.datetime.now()
    current_time  = now.strftime("%Y-%m-%d %H:%M:%S")
    hour = now.hour
    if 5 <= hour < 12:
        time_of_day = "Good Morning!"
    elif 12 <= hour < 18:
        time_of_day = "Good Afternoon!"
    else:
        time_of_day = "Good Evening!"
    quotes = [
        "Be a life long learning Person - Indira Nooyi",
        "Grow and help others to grow  -Indira Nooyi",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Strive not to be a success, but rather to be of value. - Albert Einstein",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "You don’t have to be great to start, but you have to begin. - Franklin D. Roosevelt",
        "Success is not final, failure is not fatal: It is the courage that survives through adversity and comes out successful on the other side. – Robert Schuman",
        "I believe life is an intelligent thing: that things aren't random. -Steve Jobs",
        "Black is sentimentally bad but every Black board makes the student life better -APJ ABdul Kalam ",
        "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "Do not wait to strike till the iron is hot, but make it hot by striking. - William Butler Yeats",
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
        "Success is stumbling from failure to failure with no loss of enthusiasm. - Winston Churchill",
    ]
    random_quote = random.choice(quotes)
    print(random_quote)
    return render (request, 'home.html',{'current_time': current_time,'random_quote':random_quote,'time_of_day': time_of_day})

def details(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email=request.POST.get("email")
        phone_number=request.POST.get("phone_number")
        address=request.POST.get("address")
        dob=request.POST.get("dob")
        country=request.POST.get("country")
        gender=request.POST.get("gender")
        intern_status=request.POST.get("intern_status")
        print(name,email,phone_number,address,dob,country,gender,intern_status)
        user_instance = UserDetails.objects.create(
            name=name,
            email=email,
            phone_number=phone_number,
            address=address,
            dob=dob,
            country=country,
            gender=gender,
            intern_status=intern_status
        )    
        user_instance.save()
        print(name,email,phone_number,address,dob,country,gender,intern_status)
        return HttpResponse("Thankyou for submitting the form!")
    return render(request,'details.html')
    
def dashboard(request):
    users = UserDetails.objects.all()
    return render(request, 'dashboard.html', {'users': users})