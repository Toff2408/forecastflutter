from django.urls import path, include
from .views import *

urlpatterns = [
    path('',index,name='home'),
    path('detail/info',detail,name='detail'),
]
