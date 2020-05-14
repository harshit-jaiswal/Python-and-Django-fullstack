from django.urls import path
from demo_app import views


app_name='demo_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('other/',views.other,name='other'),
]