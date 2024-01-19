from django.urls import path

from demoapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('loginview',views.loginview,name='loginview'),
    path('userhome',views.userhome,name='userhome'),
    path('add_product/',views.add_product,name='add_product'),
    path('view_product',views.view_product,name='view_product'),
    path('delete_product/<int:id>/',views.delete_product,name='delete_product'),
    path('update_product/<int:id>/',views.update_product,name='update_product'),


    ]