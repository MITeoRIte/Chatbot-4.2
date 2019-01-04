from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sendmail', views.sendmail),
    path('newgetmail/converse/',views.displaychatbot),
    path('newgetmail/converse/sendtochatterbot/',views.send_replyfromChatterbot),
    path('getmail/sendtochatterbot/', views.send_replyfromChatterbot),
    path('newgetmail/sendtochatterbot/', views.send_replyfromChatterbot),
    path('newgetmail/sendamail/', views.sendamail), 
    path('newgetmail/getamail/', views.getamail), 
    path('newgetmail/getmail/sendamail/', views.sendamail),
    path('newgetmail/', views.newgetmail),
    path('newgetmail/getmail', views.getmail),
    path('newgetmail/sendmail', views.sendmail),
    

]
