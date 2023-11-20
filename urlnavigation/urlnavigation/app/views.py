from django.shortcuts import render

# Create your views here.
def Happy(request):
    return render(request,'happy.html')

def Riya(request):
    return render(request,'riya.html')

def Happy2(request):
    return render(request,'happy2.html')

def Riya2(request):
    return render(request,'riya2.html')
    