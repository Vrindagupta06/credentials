from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Loginform, FlavorForm
from .models import Login
# Create your views here.
def create_login(request):
    if request.method == 'POST':
        form = Loginform(request.POST) 
        
        if form.is_valid():
            form.save()
            return redirect('list')
    
    else:
        form = Loginform()
    return render(request,'create.html',{'form':form})

#list view
def login_list(request):
    login = Login.objects.all()
    return render(request,'list.html',{'logins':login})

#update view
def update_login(request,pk):
    login = Login.objects.get(id=pk)
    if request.method =='POST':
        form= Loginform(request.POST, instance= login)
        
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = Loginform(instance=login)
    return render(request,'update.html',{'form':form})

#delete view
def delete_login(request, pk):
    login = Login.objects.get(id= pk)
    if request.method == "POST":
        login.delete()
        return redirect('list')
