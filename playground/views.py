import html

from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import EmailMessage, BadHeaderError
from templated_mail.mail import BaseEmailMessage

# Create your views here.


def say_hello(request):
    try:
        message = BaseEmailMessage(
            template_name="emails/hello.html",
            context={"name": "Moh"},
        )
        message.send(to=["moh@shopeasy.com"])
    except BadHeaderError:
        pass
    return render(request, "hello.html", {"name": "Moh"})
