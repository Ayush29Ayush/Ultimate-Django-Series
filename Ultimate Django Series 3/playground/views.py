from django.core.mail import send_mail, mail_admins, BadHeaderError
from django.shortcuts import render


def say_hello(request):
    try:
        # send_mail(subject="Django Test Email", message="Hello, this is a test email from django smtp server...", from_email="ayushdjango@gmail.com", recipient_list=["ayushsenapati123@gmail.com"])
        mail_admins(subject="Django Test Email", message="Hello, this is a test email from django smtp server...", fail_silently=False, html_message="Hello, this is a test email from django smtp server...")
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Ayush Senapati'})
