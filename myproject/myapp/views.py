from django.shortcuts import render,redirect
from .models import Employees

# Create your views here.
def index(request):
    emp=Employees.objects.all()
    context={
        'emp':emp
    }

    return render(request,'index.html',context)
def add(request):
    if request.method=='POST':
        email=request.POST['email']
        Name=request.POST['Name']
        address=request.POST['address']
        phone=request.POST['phone']
        employee=Employees(Name=Name,email=email,address=address,phone=phone)
        employee.save()
        return redirect('index')
    else:
        return render(request,'index.html')


def edit(request):
    emp=Employees.objects.all()
    context={
        'emp':emp
    }
    return redirect('index',context)



def update(request,id):
    emp=Employees.objects.all()
    context={
        'emp':emp
    }
    if request.method=='POST':
          email = request.POST['email']
          Name=request.POST['Name']
          address=request.POST['address']
          phone=request.POST['phone']
          employee=Employees(id=id,Name=Name,email=email,address=address,phone=phone)
          employee.save()
          return redirect('index')
    else:
        return render(request,'index.html',context)
def delete(request,id):
    if request.method=='POST':
        empp = Employees.objects.filter(id=id).delete()
        
        return redirect('index')
    else:
        emp = Employees.objects.all()
        context = {
            'emp': emp
        }
        return redirect('index', context)


