from django.db import models
from django.utils import timezone
# Create your models here


class Student(models.Model):
	faculty_no = models.CharField(max_length = 100);
	branch = models.CharField(max_length = 100);
	cpi = models.DecimalField(decimal_places=2 , max_digits=8)


class C_plus(models.Model):
	topic = models.CharField(max_length=200)
	text = models.TextField()

class BinaryTree(models.Model):
	question = models.CharField(max_length=200)
	answer = models.TextField()


