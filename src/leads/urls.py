from django.urls import path
from .views import lead_list, lead_detail, lead_create

app_name = "leads"

urlpatterns = [
    path('', lead_list, name="home"),
    path('<int:pk>/', lead_detail, name="lead_detail"),
    path('create/', lead_create, name="lead_create")
]