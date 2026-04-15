from django import forms
from appz.models import student
class stu_forms(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'