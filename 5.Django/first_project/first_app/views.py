from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello Django")

def  helpme(request):
    helpDic = {
        'details' : 'Welcome to our help Doc !'
    }
    return render(request,'first_app/index.html',context=helpDic)
