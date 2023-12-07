from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='home'),
    path('detail/<str:id>/<slug:slug>',detail,name='detail'),
]
