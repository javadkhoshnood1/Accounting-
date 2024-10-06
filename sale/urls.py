from django.urls import path
from . import views
app_name="sale"

urlpatterns =[
    path("",views.SaleView.as_view(),name="sale")
]