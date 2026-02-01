from django.shortcuts import render
from django.db import transaction
from store.models import Collection, Product, OrderItem, Order, Customer

# Create your views here.


# @transaction.atomic() # 1 this will wrap all the view with transaction
def say_hello(request):

    # 2 this give more control of which parts you want to be on transaction
    with transaction.atomic():
        order = Order()
        order.customer_id = 1  # type: ignore
        order.save()

        item = OrderItem()
        item.order = order
        item.product_id = 1  # type: ignore
        # this not work cuz no id = -1 so all the operation will refused (thats the powerful of transactions)
        # item.product_id = -1  # type: ignore
        item.quantity = 1
        item.unit_price = 10  # type: ignore
        item.save()

    return render(request, "hello.html", {"name": "moh"})
