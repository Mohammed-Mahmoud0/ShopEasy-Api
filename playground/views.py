from django.shortcuts import render
from django.db import connection
from store.models import Collection, Product, OrderItem, Order, Customer

# Create your views here.


def say_hello(request):
    # use cursor is good and give you more control of the all db 
    # method 1 but should use try final and also need to close the cursor
    cursor = connection.cursor()
    cursor.execute("select * from store_product")
    cursor.close()
    
    # method 2 is professional abd the cursor close automatically 
    with connection.cursor() as cursor:
        cursor.execute("select * from store_product")
    
    queryset = Product.objects.raw("select * from store_product")

    return render(request, "hello.html", {"name": "moh", "result": list(queryset)})
