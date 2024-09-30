from django.urls import path
from . import views
app_name = "customer"

urlpatterns =[
    path("",views.customer_list_view,name="list"),
    path("<int:id>/",views.customer_detail_view,name="detail")

]