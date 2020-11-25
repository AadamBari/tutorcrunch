from django.urls import path

from dev_test.main import views

urlpatterns = [
    path('', views.CreateOrder.as_view(), name='index'),
    path('order-confirmation/<int:pk>/', views.order_confirmation, name='order-confirmation'),

    # Create a list view
    # path('order-list/', views.ListOrders.as_view(), name='order-list'),
]
