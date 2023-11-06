from django.urls import path,include
from wine_base_marketplace import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login, name="login"),
    path('signup/',views.signup,name='signup')
]  