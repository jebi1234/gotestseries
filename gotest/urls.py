from django.urls import path,include
from . import views 

urlpatterns=[
    #path('',views.home1,name='home1'),
    #path('register',views.register,name='register'),
    #path('pali',views.pali,name='pali')
    #path('login',views.login,name='login'),
    #path('logout',views.logout,name='logout'),
    #path('booking',views.booking,name='booking')

    #path('submit',views.submit,name='submit'),
    path('',views.index,name='index.html'),
    path('starttest',views.starttest,name='starttest'),
    path('index1',views.index1,name='index1'),

    #path('essaysubmitcomponent',views.essaysubmitcomponent,name='essaysubmitcomponent.html'),
]