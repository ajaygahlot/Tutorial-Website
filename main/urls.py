from django.conf.urls import url
from .import views

urlpatterns = [
	url(r'^$',views.main,name='index'),
	url(r'^cplus/',views.C_plus_plus,name='cplus'),
	url(r'^contact/',views.contact,name='contact'),
	url(r'^binarytree/',views.binarytree,name='binarytree'),
	url(r'^student/',views.student,name='student'),
	url(r'^studentdetails/',views.studentdetails,name='studentdetails')
]