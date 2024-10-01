from django.urls import path
from . import views
app_name = "customer"

urlpatterns =[
    path("",views.customer_list_view,name="list"),
    path("<int:id>/",views.customer_detail_view,name="detail"),
    path("delete/<int:id>/",views.customer_delete_view,name="delete"),
    path("edit_price/<int:id>/",views.customer_edit_price_view,name="edit_price"),
    path("reset_price/<int:id>/",views.customer_delete_price_view,name="delete_price"),


]