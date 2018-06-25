from django import forms
from .models import Department,Employee


class AddForm(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model = Department
        fields = '__all__'

class AdForm(forms.ModelForm):
        class Meta:
            model = Employee
            fields = ('employee_name',
                      'surname',
                      'address',
                      'qualification',
                      'contact_num',
                      'department')
