from django.shortcuts import render

# Create your views here.
def Happy(request):
    return render(request,'happy.html')

def Sunny(request):
    return render(request,'sunny.html')
    