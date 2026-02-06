from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.product_list),
    path("product_details/<int:id>/", views.product_details),
    path("collections/", views.collection_list),
    path("collections/<int:pk>/", views.collection_details, name="collection-details"),
]
