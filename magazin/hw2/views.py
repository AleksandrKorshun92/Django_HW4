from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404, render
from .models import Client, Products, Order

def receive_orders(request, pk_cust):
    orders = Order.objects.filter(client=pk_cust)
    client = get_object_or_404(Client, pk=pk_cust)
    products = {}
    for order in orders:
        prod_list = []
        order_prods = order.orders.all()
        for prod in order_prods:
            prod_list.append(prod.name)
        products[order.pk] = set(prod_list)
    context = {"orders": orders, "products": products, "client": client}
    return render(request, "hw2/orders.html", context)

def orders_story(request, pk_cust, days):
    customer = Client.objects.filter(pk=pk_cust).first()
    ord = Order.objects.filter(client=pk_cust)
    my_date = datetime.now() - timedelta(days=days)
    order_list = ord.filter(created__gte=my_date, created__lte=datetime.now())
    prods_dict = {}
    for order in order_list:
        prods = order.orders.all()
        prods_dict[order] = set(prods)
    context = {
        "prods_dict": prods_dict,
        "customer": customer,
        "days": days,
    }

    return render(request, "hw2/orders_story.html", context)
