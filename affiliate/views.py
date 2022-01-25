from concurrent.futures.process import _python_exit
import email
from unicodedata import name
from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == "POST":
        m_name = request.POST['name']
        m_email = request.POST['email']
        m_phone = request.POST['phone']
        m_message = request.POST['message']

        send_mail(
            m_name, # subject
            m_message, # message
            m_email, # from email
            ['mrbigben61@gmail.com'], # to email
        )

        return render(request, 'contact.html', {'m_name': m_name})

    else:
        return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})

def pricing(request):
    return render(request, 'pricing.html', {})