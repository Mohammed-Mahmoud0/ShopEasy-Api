import html

from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail, mail_admins, BadHeaderError

# Create your views here.


def say_hello(request):
    try:
        mail_admins(
            "subject here",
            "Here is the message.",
            html_message="message in html",
        )
    except BadHeaderError:
        pass
    return render(request, "hello.html", {"name": "Moh"})
