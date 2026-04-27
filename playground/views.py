from django.shortcuts import render
import logging
import requests

logger = logging.getLogger(__name__)


def say_hello(request):
    try:
        logger.info("calling httpbin")
        response = requests.get("https://httpbin.org/delay/2")
        logger.info("httpbin responded with status code %s", response.status_code)
        data = response.json()
    except requests.ConnectionError:
        logger.critical("httpbin is not responding")
    return render(request, "hello.html", {"name": data})
