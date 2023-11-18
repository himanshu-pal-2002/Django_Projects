from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':12}
    return render(request,'condition.html',d)

def ifelse(request):
    d={'a':10,'b':20}
    return render(request,'ifelse.html',d)

def ifelif(request):
    d={'a':10,'b':200,'c':30}
    return render(request,'ifelif.html',d)


def nestedif(request):
    d={'a':10,'b':200,'c':30}
    return render(request,'nestedif.html',d)
    
    
    