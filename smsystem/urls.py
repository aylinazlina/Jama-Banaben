"""
URL configuration for smsystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from jamaZZZ import views as j_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',j_view.home,  name='home'),
    path('<str:pk>',j_view.itemDetails,name ='itemDetails'),
    path('createItem/',j_view.createItem,name='createItem'),
    path('updateItem/<str:pk>',j_view.updateItem,name='updateItem'),
    path('deleteItem/<str:pk>',j_view.deleteItem,name='deleteItem'),
    path('women/',j_view.women, name='women'),
    path('women/<str:pk>/',j_view.womenDetails,name ='womenDetails'),
    path('men/',j_view.men, name='men'),
    path('men/<str:pk>/',j_view.MenDetails,name ='MenDetails'),
    path('designer/',j_view.designer, name='designer'),
    path('cart/',j_view.cart, name='cart'),
    path('add_to_cart/<int:product_id>/', j_view.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:item_id>/', j_view.remove_from_cart, name='remove_from_cart'),
    path('orders/', j_view.orders, name='orders'),
    path('orderForm/', j_view.add_orders, name='orderForm'),
    path('contact/',j_view.contact,name='contact'),
    path('registration/',j_view.Registration,name='Registration'),
    path('login/',j_view.loginPage,name='loginPage'),
    path('logout/', j_view.logoutuser, name='logoutuser'),
    path('user/',j_view.userPage,name='userPage'),
    path('userProfile/',j_view.userProfile,name='userProfile'),

    path('profileForm/', j_view.userProfile_add, name='profileForm'),
    path('profileForm/edit_profile/', j_view.edit_profile, name='edit_profile')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

