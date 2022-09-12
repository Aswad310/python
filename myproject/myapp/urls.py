from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('contact/', views.contact),
    path('product/<number>', views.product),
    path('productday/<month>/<year>', views.productday),
    path('hello/', views.hello),
]