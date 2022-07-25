from django.urls import path
from . import views

urlpatterns = [
    path('new_page',views.new_page)
]
