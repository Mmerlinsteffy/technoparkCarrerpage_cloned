from django.shortcuts import render
from . models import Job
# Create your views here.
def home(request):
    details=Job.objects.all
    return render(request,'home.html',{'jobs':details})
def globcom(request,id):
    details=Job.objects.get(id=id)
    return render(request,'globcom.html',{'detail':details})