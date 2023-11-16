from django.shortcuts import render


# Create your views here.
def Rohit(request):
    data='India win 3rd Time 50 Over World Cup'
    d={'himanshu':data}
    return render(request,'rohit.html',context=d)

def Msd(request):
    data='India win 2nd Time 50 Over World Cup'
    m={'himanshu':data}
    return render(request,'msd.html',context=m)

def KapilDev(request):
    data='India win Ist Time 50 Over World Cup'
    k={'himanshu':data}
    return render(request,'kapil.html',context=k)