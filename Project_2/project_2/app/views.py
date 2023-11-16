from django.shortcuts import render


# Create your views here.
def Rohit(request):
    data='India win 3rd Time 50 Over World Cup'
    d={'himanshu':data}
    
    return render(request,'rohit.html',context=d)