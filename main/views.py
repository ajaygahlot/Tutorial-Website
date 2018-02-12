from django.shortcuts import render
from .forms import ContactForm,StudentForm,studentdetailForm
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import redirect
from .models import C_plus,BinaryTree,Student
from django.utils import timezone
from django.core.mail import EmailMessage
# Create your views here.
def main(request):
	return render(request,'base.html')

def C_plus_plus(request):
	cplus = C_plus.objects.all()
	context = {
		'cplus':cplus,
	} 
	return render(request,'main/cplus.html',context)


def binarytree(request):
	tree = BinaryTree.objects.all()
	context = {
		'tree':tree,
	} 
	return render(request,'main/trees.html',context)

def contact(request):
	form_class = ContactForm
	if request.method == 'POST':
		form = form_class(data=request.POST)
		if form.is_valid():
			contact_name = request.POST.get('contact_name', '')
			contact_email = request.POST.get('contact_email', '')
			form_content = request.POST.get('content', '')

            # Email the profile with the 
            # contact information
			template = get_template('contact_template.txt')
           	context = {'contact_name': contact_name,'contact_email': contact_email,'form_content': form_content,}
           	content = template.render(context)
           	email = EmailMessage(
				"New contact form submission",content,"Your website" +'',['youremail@gmail.com'],headers = {'Reply-To': contact_email })
           	email.send()
           	return render(request,'main/contact_complete.html')

	return render(request, 'main/contact.html', {'form': form_class})


def student(request):
	if request.method == "POST":
		form = StudentForm(request.POST)
		if form.is_valid():
			stud = form.save(commit = False)
			stud.save()
			return redirect('index')
	else:
		form = StudentForm()
	return render(request,'main/studentform.html',{'form':form})


def studentdetails(request):
	flag = False
	stud = Student.objects.all()
	if request.method == 'POST':
		form = studentdetailForm(request.POST)
		if form.is_valid():
			text = form.cleaned_data['faculty_no']
			for s in stud:
				if s.faculty_no == text:
					flag = True
					break
			if flag == True:
				context = {'form':form,'s':s,'flag':flag}
				return render(request,'main/studentdetail.html',context)
			else:
				return render(request,'main/studentdetail.html',{'message':'username does not exist' , 'form':form,'flag':flag})
	else:
		form = studentdetailForm()
	return render(request,'main/studentdetail.html',{'form':form})




