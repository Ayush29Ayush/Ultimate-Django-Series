from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage
from django.shortcuts import render


def say_hello(request):
    try:
        message = EmailMessage(
            subject="Django Test Email",
            body="Hello, this is a test email from django smtp server...",
            from_email="ayushdjango@gmail.com",
            to=["ayushsenapati123@gmail.com"],
        )
        message.attach_file("playground/static/images/amazon.png")
        message.send()
    except BadHeaderError:
        pass

    return render(request, "hello.html", {"name": "Ayush Senapati"})
