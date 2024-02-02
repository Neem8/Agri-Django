from django.shortcuts import render,redirect
from .models import Farmer,Product,Catogery,SubCatogery
import random
import os
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from .forms import FarmerForm,ProductForm

# Create your views here.

#--------------------------------------------------------------------------------
# Index -------------------------
#________________________________________________________________________________

def index(request):
    try:
        if(request.session):
            current_user = Farmer.objects.get(farmer_email=request.session['farmer_email'])
            return render(request, 'index.html',{'current_user':current_user})
    except:
        return render(request, 'index.html')

#--------------------------------------------------------------------------------
# Index -------------------------
#________________________________________________________________________________




#--------------------------------------------------------------------------------
# Sign Up and Sign in
#________________________________________________________________________________

def register(request):
    if request.method == 'POST':
        global User_data
        User_data = FarmerForm(data=request.POST,files=request.FILES)
        if request.POST['farmer_password'] == request.POST['farmer_repassword']:
            global otp_sent
            otp_sent = random.randint(1000,9999)
            message = f"""Hi your OTP is {otp_sent}."""	
            subject = 'BlogSpot Registration.'
            from_email = settings.EMAIL_HOST_USER

            send_mail(subject, message, from_email,[request.POST['farmer_email']])
            return render(request, 'otp.html', {'msg':'Check Your Mail For Otp','otp_sent':otp_sent}) 
        else:
            return render(request,'register.html', {'msg':'Passwords do not match!!!!!!!!'})
    else:
        return render(request,'register.html')

def otp(request):
    if request.method == 'POST':
        recieved_otp = request.POST['recieved_otp']
        if int(recieved_otp) == otp_sent:
            if User_data.is_valid():
                User_data.save()
                return render(request, 'login.html', {'msg':'Your Account has been created Successfully !!!!! \n Kindly Login'})
        else:
            return render(request, 'otp.html', {'msg':'Invalid OTP'})
    else:
        return render(request, 'otp.html')

def login(request):
        try:
            current_user = Farmer.objects.get(farmer_email=request.POST['farmer_email_check'])
            try:
                current_user.farmer_password == request.POST['farmer_password_check']
                request.session['farmer_email'] = current_user.farmer_email
                return render(request, 'index.html',{"current_user":current_user})
            except Farmer.DoesNotExist:
                return render(request, 'login.html', {'msg':'Invalid Credentials !!!!!'})
        except:
            return render(request, 'login.html')

def logout(request):
    del request.session['farmer_email']
    return redirect('index')
#--------------------------------------------------------------------------------
# Sign Up and Sign in
#________________________________________________________________________________


def challan(request):
    row_range=range(1,13)
    col_range=range(1,7)


    try:
        total = 0
        for i in row_range:
            for j in col_range:
                val =str(i)+str(j)
                value=request.POST[val]
                if value:
                    total = total + int(value)
        print(total)
    except:
        return render(request,'challan.html',context={'row_range':row_range,'col_range':col_range})
    return render(request,'challan.html',context={'row_range':row_range,'col_range':col_range})




#--------------------------------------------------------------------------------
# Products ------------------------------
#________________________________________________________________________________
def products(request):
        list_of_products = Product.objects.all()
        return render(request, 'products.html',{"list_of_products":list_of_products})
#--------------------------------------------------------------------------------
# Products ------------------------------
#________________________________________________________________________________

def addproduct(request):
    return render(request, 'addproduct.html')

def profile(request):
    try:
        current_user = Farmer.objects.get(farmer_email=request.session['farmer_email'])
        if request.method == 'POST':
            current_user.farmer_name = request.POST['farmer_name']
            current_user.farmer_phone = request.POST['farmer_phone']
            current_user.farmer_address = request.POST['farmer_address']  
            try:
                current_user.farmer_profile_pic = request.FILES['image']       
            except:
                pass
            current_user.save()
            return render(request, 'profile.html',{'current_user':current_user,'msg':"Updated Successfully"})

        else:
            return render(request, 'profile.html',{'current_user':current_user})
    except:
        return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')



def admin_login(request):
    return HttpResponse(admin_login)