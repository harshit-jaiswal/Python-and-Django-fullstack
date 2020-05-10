from django.shortcuts import render
from first_app.models import  Topic, Webpage, AccessRecord

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    data_dict = {'access_records':webpages_list}
    return render(request, 'first_app/startup_page.html', context=data_dict)

def  helpme(request):

    help_dic = {
        'details' : 'Welcome to our help Doc !'
    }
    return render(request, 'first_app/index.html', context=help_dic)
