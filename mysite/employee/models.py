from django.db import models

class Department(models.Model):
    name = models.CharField(max_length= 20,null=True)
    def __str__(self):
        return self.name


class Employee(models.Model):
    employee_name = models.CharField(max_length= 20, null=True)
    surname = models.CharField(max_length= 20, null=True)
    address = models.CharField(max_length  = 50, null=True)
    qualification = models.CharField(max_length = 30,null=True)
    contact_num = models.IntegerField(null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self):
        return self.employee_name

