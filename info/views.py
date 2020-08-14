from django.shortcuts import render
from info.models import *


# Create your views here.
def home(request):
    return render(request, 'info/index.html')

def about(request):
	return render(request, 'info/about.html')

def admission(request):
	return render(request, 'info/admission.html')

def faculty(request):
    teacher = Teacher.objects.all()
    context = {'teacher':teacher}
    return render(request, 'info/faculty.html',context)

def campus(request):
	return render(request, 'info/campus.html')

def contact(request):
	return render(request, 'info/contact.html')

def gallary(request):
	return render(request, 'info/gallary.html')


def notice(request):
    notice = Notice.objects.all()
    context = {'notice':notice}
    return render(request, 'info/notice.html', context)

def pride(request):
	return render(request, 'info/pride.html')
