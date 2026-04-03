import html

from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import EmailMessage, BadHeaderError

# Create your views here.


def say_hello(request):
    try:
        message = EmailMessage(
            "subject", "message", "from@shopeasy.com", ["moh@shopeasy.com"]
        )
        message.attach_file("playground/static/images/download.jpg")
        message.send()
    except BadHeaderError:
        pass
    return render(request, "hello.html", {"name": "Moh"})
