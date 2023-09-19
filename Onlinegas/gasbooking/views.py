from django.shortcuts import render,HttpResponse,redirect
from .models import *
# Create your views here.
def homepage(request):
    return render(request,'homepage.html')

def login(request):
    return render(request,'login.html')

def signupform(request):
    return render(request,'signupform.html')

def mainpage(request):
    return render(request,'main page.html')

def service(request):
    return render(request,'service.html')

def client(request):
    return render(request,'client.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
def justbefore(request):
    return render(request,'justbefore.html')
def clientafterlogin(request):
    return render(request,'clientafterlogin.html')

def adminafterlogin(request):
    return render(request,'adminafterlogin.html')

def save_client(request):
    c = Client_details()
    c.fullname = request.POST.get('fullname')
    c.email = request.POST.get('email')
    c.address = request.POST.get('address')
    c.mobile_no = request.POST.get('mobile_no')
    c.username = request.POST.get('username')
    c.password = request.POST.get('password')
    c.save()

    return redirect('justbefore')

def save_admin(request):
    a = Admin_details()
    a.username = request.POST.get('username')
    a.password = request.POST.get('password')
    a.email = request.POST.get('email')
    a.address = request.POST.get('address')
    a.mobile_no = request.POST.get('mobile_no')
    a.fullname = request.POST.get('fullname')
    a.save()

    return redirect('justbefore')

def client_list(request):
    Client_data = Client_details.objects.all()
    return render(request, 'show_register_user.html', {'Client_data': Client_data})

# def client_data(request,pk):
#     Client = Client_details.objects.get(id=pk)
#     return render(request, '.html', {'Client': Client})




def admin_list(request):
    Admin_data = Admin_details.objects.all()
    return render(request, 'show_register_admin.html', {'Admin_data': Admin_data})

# def admin_data(request,pk):
#     Admin = Client_details.objects.get(id=pk)
#     return render(request, '.html', {'Admin': Admin})
def choice(request):
    return render(request,'choice_details_registration.html')
def reg_admin(request):
    return render(request,'reg_admin.html')
def reg_client(request):
    return render(request,'reg_client.html')

def log_admin(request):
    return render(request,'log_admin.html')

def log_client(request):
    return render(request,'log_client.html')


