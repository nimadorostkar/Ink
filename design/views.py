from django.shortcuts import render
from homepage.models import HomepageInfo
from design.models import Design


def portfolio(request):
    data = HomepageInfo.objects.all().first()
    portfolio = Design.objects.all().order_by('-id')
    context = {'data':data,'portfolio':portfolio}
    return render(request, 'portfolio.html', context)
