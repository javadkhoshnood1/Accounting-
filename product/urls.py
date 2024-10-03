from django.urls import path 
from . import views
app_name = "product"

urlpatterns =[
    path("",views.product_list_view,name="list"),
    path("<int:id>/",views.product_detail_view,name="detail"),
    path("add_category/",views.add_category_view,name="add_category"),
    path("delete/<int:id>/",views.delete_product_view,name="delete"),
    path("category/<int:id>/",views.category_list_view,name="list_category")
]