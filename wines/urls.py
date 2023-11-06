
from django.urls import path,include
from wines import views

urlpatterns = [
    path('',views.helloworld),
]    