"""
URL configuration for babycare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from lullaby import views

from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    
    path('admin/', admin.site.urls),

    path('register/',views.RegistrationView.as_view(),name='register'),

    path('',views.LoginView.as_view(),name='signin'),

    path('index/',views.IndexView.as_view(),name='index'),

    path('products/detail/<int:pk>/',views.ProductDetailView.as_view(),name='product-detail'),

    path('product/<int:pk>/cart/add/',views.AddToCartview.as_view(),name='addtocart'),

    path('carts/all/',views.CartSummaryView.as_view(),name='cart-summary'),

    path('basketitem/<int:pk>/remove',views.CartItemDestroy.as_view(),name='cart-remove'),

    path('signout/',views.SignOutView.as_view(),name='signout'),

    path('basketitem/quantity/<int:pk>/change',views.CartQuantityUpdateView.as_view(),name='quantity-update'),

    path('order/add/',views.PlaceOrderView.as_view(),name="place-order"),

    path('order/summary',views.OrderSummaryView.as_view(),name='order-summary'),

    path('home/',views.HomeView.as_view(),name='home')


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

