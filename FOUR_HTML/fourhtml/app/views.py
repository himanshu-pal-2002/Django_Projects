from django.shortcuts import render

# Create your views here.
def First_Page(request):
    return render(request,'first.html')

def Second_Page(request):
    return render(request,'second.html')

def Third_Page(request):
    return render(request,'third.html')

def Fourth_Page(request):
    return render(request,'fourth.html')
