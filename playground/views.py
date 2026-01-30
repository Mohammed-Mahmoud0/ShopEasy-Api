from django.shortcuts import render
from django.db.models.aggregates import Avg, Count, Max, Min, Sum
from django.db.models import Value, F, Func
from django.db.models.functions import Concat
from store.models import Product, OrderItem, Order, Customer

# Create your views here.


def say_hello(request):
    queryset = Customer.objects.annotate(num_orders=Count("order"))

    return render(request, "hello.html", {"name": "moh", "result": queryset})
