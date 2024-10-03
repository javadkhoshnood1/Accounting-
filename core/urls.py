from django.contrib import admin
from django.urls import path,include, re_path
from django.conf.urls.static import static
from core.settings import MEDIA_URL
from core.settings import MEDIA_ROOT
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("home.urls")),
    path("dashboard/",include("accounts.urls")),
    path("customers/",include("customer.urls")),
    path("contact/",include("contact.urls")),
    path("products/",include("product.urls"))

]+ static(MEDIA_URL, document_root=MEDIA_ROOT)
