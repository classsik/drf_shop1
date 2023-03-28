from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),

    path('products/', views.get_products),
    path('products/create/', views.create_product),
    path('products/<int:pk>/edit/', views.edit_product),
    path('products/<int:pk>/delete/', views.get_products),

    path('add_to_cart/<int:product_id>/', views.add_to_cart),
    path('order/create/', views.create_order)
]
