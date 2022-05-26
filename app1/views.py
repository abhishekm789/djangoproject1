import email
from django.http import HttpResponse
from django.shortcuts import redirect,render
from numpy import place
from app1.models import Register
from app1.forms import RegisterForm,LoginForm,UpdateForm
from django.contrib import messages

# Create your views here.
def hello(request):
    return render(request,'index.html')

def index(request):
    name="Abhishek"
    return render(request,'index.html',{'data':name})

def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            place=form.cleaned_data['Place']
            photo=form.cleaned_data['Photo']
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            cpassword=form.cleaned_data['Confirmpassword']

            user=Register.objects.filter(Email=email).exists()
            if user:
                messages.warning(request,"Email already exists.")
                return redirect('/register')
            elif password!=cpassword:
                messages.warning(request,"Password Mismatch!")
                return redirect('/register')
            else:
                tab=Register(Name=name,Age=age,Place=place,Photo=photo,Email=email,Password=password)
                tab.save()
                return redirect('/')

    else:
        form=RegisterForm()
    return render(request,'register.html',{'form':form})

def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            user=Register.objects.get(Email=email)
            if not user:
                messages.warning(request,"Email does'nt exist.")
                return redirect('/login')
            elif password!=user.Password:
                messages.warning(request,"Password Mismatch!")
                return redirect('/login')   
            else:
                messages.success(request,"Login Successful!")
                return redirect('/home/%s' % user.id)
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})

def home(request,id):
    data=Register.objects.get(id=id)
    return render(request,'home.html',{'data':data})
    
def update(request,id):
    user=Register.objects.get(id=id)
    if request.method=='POST':
        form=UpdateForm(request.POST or None,request.FILES or None,instance=user)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            place=form.cleaned_data['Place']
            photo=form.cleaned_data['Photo']
            email=form.cleaned_data['Email']
            form.save()
            return redirect('/home/%s' % user.id)
    else:
        form=UpdateForm(instance=user)
    return render(request,'update.html',{'form':form,'user':user})

