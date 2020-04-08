from django.shortcuts import render,redirect
from .models import Service,Portfolio,About,Team,Contact
from django.contrib import messages
# Create your views here.
def home (request):
    service = Service.objects.all()
    portfolio = Portfolio.objects.all()
    about = About.objects.order_by('-a_date')
    team = Team.objects.all()
    context = {
        'service': service,
        'portfolio': portfolio,
        'about': about,
        'team': team,
    }
    return render(request,'portfolio/home.html', context)

def single_portfolio(request,id):
    single = Portfolio.objects.filter(pk=id)
    context = {
        'single': single,
    }
    return render(request, 'portfolio/single_portfolio.html', context)

def contact(request):
    if request.method=='POST':
        cnt = Contact(
        c_name=request.POST['name'],
        c_email=request.POST['email'],
        c_phone=request.POST['phone'],
        c_message=request.POST['message'],
    )
        cnt.save()
        messages.success(request, 'message send successfully')
    return redirect('home')