from django.urls import path
from .views import receive_orders, orders_story

urlpatterns = [
    path("orders/<int:pk_cust>/", receive_orders, name="receive_orders"),
    path("story/<int:pk_cust>/<int:days>/", orders_story, name="orders_story"),
]