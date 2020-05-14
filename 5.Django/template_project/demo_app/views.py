from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'harshit jaiswal','number':101}
    return render(request,'demo_app/index.html',context_dict)

    
def other(request):
    return render(request,'demo_app/others.html')

