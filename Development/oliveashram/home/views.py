from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request,'about.html')
def mission(request):
    return render(request,'mission.html')
def news(request):
    return render(request,'news.html')
def services(request):
    return render(request,'services.html')
def history(request):
    return render(request,'about-history.html')
def charism(request):
    return render(request,'about-charism.html')
def founder(request):
    return render(request,'about-founder.html')
def members(request):
    return render(request,'about-members.html')
def vision(request):
    return render(request,'mission-vision.html')    