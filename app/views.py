from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q

# Create your views here.

def home_page(request):
    val=Employee.objects.all()
    if request.method == 'POST':
        value=request.POST.get('search')
        sr=Employee.objects.filter(Q(first_name__icontains=value))
        return render(request,'home.html',{'data':sr})
    return render(request,'home.html',{'data':val})
def popup_page(request):
    if request.method == 'POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        dep=request.POST.get('dptmnt')
        desig=request.POST.get('dsg')
        date=request.POST.get('doj')
        sal=request.POST.get('sal')
        img=request.FILES.get('profile')
        obj=Employee()
        obj.first_name=fname
        obj.last_name=lname
        obj.department=dep
        obj.designation=desig
        obj.date_of_joining=date
        obj.salary=sal
        obj.profile_image=img
        obj.save()
        return redirect('home')
    return render(request,'popup.html')
def delete_employee(request,id):
    data=Employee.objects.get(id=id)
    data.delete()
    return redirect('home')
def edit_profile(request,id):
    obj=Employee.objects.get(id=id)
    if request.method == 'POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        dep=request.POST.get('dptmnt')
        desig=request.POST.get('dsg')
        date=request.POST.get('doj')
        sal=request.POST.get('sal')
        img=request.FILES.get('profile')
        if img == None:
            img=obj.profile_image
        obj.first_name=fname
        obj.last_name=lname
        obj.department=dep
        obj.designation=desig
        obj.date_of_joining=date
        obj.salary=sal
        obj.profile_image=img
        obj.save()
        return redirect('home')
    return render(request,'edit_profile.html',{'data':obj})
