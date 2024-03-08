from django.shortcuts import render
from homepage.models import HomepageInfo
from contact.models import ContactMessage


def index(request):
    data = HomepageInfo.objects.all().first()
    if request.method == 'POST':
        msg = ContactMessage()
        msg.name = request.POST['name']
        msg.email = request.POST['email']
        msg.message = request.POST['message']
        msg.save()
    context = {'data':data}
    return render(request, 'index.html', context)
