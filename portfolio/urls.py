from django.contrib import admin
from django.urls import path
from .views import home, single_portfolio, contact
urlpatterns = [
    path('',home,name='home'),
    path('contact',contact,name='contact'),
    path('portfolio/<int:id>',single_portfolio,name='single'),

]
