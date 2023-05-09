from django.urls import path
from . import views
from django.urls import path
from .views import CustomerListCreateView, CustomerRetrieveUpdateDestroyView, \
                   ProductListCreateView, ProductRetrieveUpdateDestroyView, \
                   ProductActivateDeactivateView

urlpatterns = [
    path('customers/', CustomerListCreateView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroyView.as_view(), name='customer-detail'),
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    path('products/<int:pk>/activate-deactivate/', ProductActivateDeactivateView.as_view(), name='product-activate-deactivate'),
]
