from django.shortcuts import render
from .forms import StudentForm
# Create your views here.
from .models import SData

def homepage(request):
    if request.method=='POST':
        student=StudentForm(request.POST)
        if student.is_valid():
            SData(
            sname=request.POST.get('sname'),
            sage=request.POST.get('sage'),
            smobile=request.POST.get('smobile'),
            ).save()
            return render(request,'home.html',{'student':student})
    else:
        student=StudentForm()
        return render(request,'home.html',{'student':student})
