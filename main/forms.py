from django import forms
from .models import Student

class ContactForm(forms.Form):
	contact_name = forms.CharField(required = True)
	contact_email = forms.EmailField(required = True)
	content = forms.CharField(required=True , widget=forms.Textarea)

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ('faculty_no','branch','cpi')

class studentdetailForm(forms.Form):
	faculty_no = forms.CharField(required = True)
