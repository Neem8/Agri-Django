from django.shortcuts import render
from .models import Admin
import random
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse


# Create your views here.


#--------------------------------------------------------------------------------
# Sign Up and Sign in
#________________________________________________________________________________

def admin_register(request):
    if request.method == 'POST':
        global User_data
        User_data = {"admin_name" : request.POST['admin_name'],
                     "admin_email" : request.POST['admin_email'],
                     "admin_phone" : request.POST['admin_phone'],
                     "admin_address" : request.POST['admin_address'],
                     "admin_password" : request.POST['admin_password'],
                     "admin_repassword" : request.POST['admin_repassword']
                     }
        if User_data['admin_password'] == User_data['admin_repassword']:
            global otp_sent
            otp_sent = random.randint(1000,9999)
            message = f"""Hi your OTP is {otp_sent}."""	
            subject = 'Admin Registration.'
            from_email = settings.EMAIL_HOST_USER

            send_mail(subject, message, from_email,[User_data['admin_email']])
            return render(request, 'admin_otp.html', {'msg':'Check Your Mail For Otp',otp_sent:otp_sent}) 
        else:
            return render(request,'admin_register.html', {'msg':'Passwords do not match!!!!!!!!'})
    else:
        return render(request,'admin_register.html')

def admin_otp(request):
    if request.method == 'POST':
        recieved_otp = request.POST['recieved_otp']
        if int(recieved_otp) == otp_sent:
            admin=Admin.objects.create(admin_name=User_data['admin_name'],admin_email=User_data['admin_email'],admin_phone=User_data['admin_phone'],admin_address=User_data['admin_address'],admin_password=User_data['admin_password'])

            return render(request, 'admin_login.html', {'msg':'Your Account has been created Successfully !!!!! \n Kindly Login'})
        else:
            return render(request, 'admin_otp.html', {'msg':'Invalid OTP'})
    else:
        return render(request, 'admin_otp.html')

def admin_login(request):
    if request.method == 'POST':

        try:
            current_user = Admin.objects.get(admin_email=request.POST['admin_email_check'])
            print("user is present")
            if current_user.admin_password == request.POST['admin_password_check']:
                request.session['admin_email'] = current_user.admin_email
                return HttpResponse("Login Successfull")
        except Admin.DoesNotExist:
            return render(request, 'admin_login.html', {'msg':'Invalid Credentials !!!!!'})
    else:
        return render(request,'admin_login.html')

#--------------------------------------------------------------------------------
# Sign Up and Sign in
#________________________________________________________________________________