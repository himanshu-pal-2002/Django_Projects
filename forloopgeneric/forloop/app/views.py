from django.shortcuts import render

# Create your views here.
def forloop(request):
    d={'Name':['Himanshu','Aakash','Nihal']}
    return render(request,'forloop.html',d)