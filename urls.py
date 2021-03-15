
from django.contrib import admin
from django.urls import path
from compilerapp import views
urlpatterns = [
   path('test/',views.index,name='test'),
]
