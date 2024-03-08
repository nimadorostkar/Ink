from django.shortcuts import render
from homepage.models import HomepageInfo
from contact.models import ContactMessage
from design.models import Design


def index(request):
    data = HomepageInfo.objects.all().first()
    portfolio = Design.objects.filter(portfolio_homepage=True).order_by('-id')[:10]
    if request.method == 'POST':
        msg = ContactMessage()
        msg.name = request.POST['name']
        msg.email = request.POST['email']
        msg.message = request.POST['message']
        msg.save()
    context = {'data':data,'portfolio':portfolio}
    return render(request, 'index.html', context)
