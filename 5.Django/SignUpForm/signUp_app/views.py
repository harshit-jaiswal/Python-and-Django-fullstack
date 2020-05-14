from django.shortcuts import render
from signUp_app.forms import NewUserForm

# Create your views here.
def index(request):
    form = NewUserForm()
    if request.method =="POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print('Error Form Invaild!!')
    return render(request,'signUp_app/index.html',{'form':form})            