from first_app import views
from django.conf.urls import url
from django.urls import path
urlpatterns = [
    path('',views.index,name='index'),
    path('help/',views.helpme,name='help')
]