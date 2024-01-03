from django.shortcuts import render
# from app.forms import NameForm

# Create your views here.
def School(request):
    return render(request,'home.html')