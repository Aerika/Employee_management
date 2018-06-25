from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .form import *
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

def department_list(request):
    department = Department.objects.all()
    department_name = list()

    for i in department:
        department_name.append(i.name)
    return render(request, 'employee/department_list.html', {'department' : department})

def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('department-list'))
    else:
        form = AddForm()

    return render(request, 'employee/add.html', {'form': form})

def d_delete(request, pk):
    p = get_object_or_404(Department, pk=pk)
    if request.method == "POST":
        form = AddForm(request.POST, instance=p)
        if form.is_valid():
            p = form.save(commit=False)
            p.delete()
            return redirect('department-list')
    else:
        form = AddForm(instance=p)
    return render(request, 'employee/delete.html', {'form': form})


def d_edit(request, pk):
    p = get_object_or_404(Department, pk=pk)
    if request.method == "POST":
        form = AddForm(request.POST, instance=p)
        if form.is_valid():
            p = form.save(commit=False)
            p.save()
            return redirect('department-list')
    else:
        form = AddForm(instance=p)
    return render(request, 'employee/add.html', {'form': form})

def employee_list(request):
    employee = Employee.objects.all()
    employees = list()

    for i in employee:
        employees.append(i.employee_name)
        employees.append(i.surname)
        employees.append(i.address)
        employees.append (i.qualification)
        employees.append (i.contact_num)
       # employees.append (i.department)
    return render(request, 'employee/employee_list.html', {'employee' : employee})


def create(request):
    if request.method == 'POST':
        form = AdForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('employee-list'))
    else:
        form = AdForm()

    return render(request, 'employee/create.html', {'form': form})

def delete(request, pk):
    p = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        form = AdForm(request.POST, instance=p)
        if form.is_valid():
            p = form.save(commit=False)
            p.delete()
            return redirect('employee-list')
    else:
        form = AdForm(instance=p)
    return render(request, 'employee/delete.html', {'form': form})


def edit(request, pk):
    p = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        form = AdForm(request.POST, instance=p)
        if form.is_valid():
            p = form.save(commit=False)
            p.save()
            return redirect('employee-list')
    else:
        form = AdForm(instance=p)
    return render(request, 'employee/create.html', {'form': form})