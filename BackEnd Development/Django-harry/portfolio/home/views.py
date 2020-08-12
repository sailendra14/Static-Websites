from django.shortcuts import render
from django.http import HttpResponse
from home.models import Contact
# Create your views here.


def index(request):
    context = {'name': 'Sai', 'age': 100}
    return render(request, 'index.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        print('the has neen written into the database')
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def project(request):
    return render(request, 'project.html')
