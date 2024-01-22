from django.shortcuts import render
from .models import Farmer,Product,Catogery,SubCatogery
import random
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse


# Create your views here.

#--------------------------------------------------------------------------------
# Index -------------------------
#________________________________________________________________________________

def index(request):
    current_user = Farmer.objects.get(farmer_email=request.session['farmer_email'])
    if current_user:
        print(current_user)
    return render(request, 'index.html',{'current_user':current_user})

#--------------------------------------------------------------------------------
# Index -------------------------
#________________________________________________________________________________




#--------------------------------------------------------------------------------
# Sign Up and Sign in
#________________________________________________________________________________

def register(request):
    if request.method == 'POST':
        global User_data
        User_data = {"farmer_name" : request.POST['farmer_name'],
                     "farmer_email" : request.POST['farmer_email'],
                     "farmer_phone" : request.POST['farmer_phone'],
                     "farmer_address" : request.POST['farmer_address'],
                     "farmer_password" : request.POST['farmer_password'],
                     "farmer_repassword" : request.POST['farmer_repassword']
                     }
        if User_data['farmer_password'] == User_data['farmer_repassword']:
            global otp_sent
            otp_sent = random.randint(1000,9999)
            message = f"""Hi your OTP is {otp_sent}."""	
            subject = 'BlogSpot Registration.'
            from_email = settings.EMAIL_HOST_USER

            send_mail(subject, message, from_email,[User_data['farmer_email']])
            return render(request, 'otp.html', {'msg':'Check Your Mail For Otp',otp_sent:otp_sent}) 
        else:
            return render(request,'register.html', {'msg':'Passwords do not match!!!!!!!!'})
    else:
        return render(request,'register.html')

def otp(request):
    if request.method == 'POST':
        recieved_otp = request.POST['recieved_otp']
        if int(recieved_otp) == otp_sent:
            farmer=Farmer.objects.create(farmer_name=User_data['farmer_name'],farmer_email=User_data['farmer_email'],farmer_phone=User_data['farmer_phone'],farmer_address=User_data['farmer_address'],farmer_password=User_data['farmer_password'])

            return render(request, 'login.html', {'msg':'Your Account has been created Successfully !!!!! \n Kindly Login'})
        else:
            return render(request, 'otp.html', {'msg':'Invalid OTP'})
    else:
        return render(request, 'otp.html')

def login(request):
    if request.method == 'POST':

        try:
            current_user = Farmer.objects.get(farmer_email=request.POST['farmer_email_check'])
            print("user is present")
            if current_user.farmer_password == request.POST['farmer_password_check']:
                request.session['farmer_email'] = current_user.farmer_email
                return render(request, 'index.html',{"current_user":current_user})
        except Farmer.DoesNotExist:
            return render(request, 'login.html', {'msg':'Invalid Credentials !!!!!'})

        return render(request, 'login.html')
#--------------------------------------------------------------------------------
# Sign Up and Sign in
#________________________________________________________________________________






#--------------------------------------------------------------------------------
# Products ------------------------------
#________________________________________________________________________________
def products(request):
        list_of_products = Product.objects.all()
        return render(request, 'products.html',{"list_of_products":list_of_products})
#--------------------------------------------------------------------------------
# Products ------------------------------
#________________________________________________________________________________



def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')


def admin_login(request):
    return HttpResponse(admin_login)