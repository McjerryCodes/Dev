from django.urls import path
from .views import ProductListCreateView
from.views import ProductRetrieveDeleteUpdateView 

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product'),
    path('products/', ProductRetrieveDeleteUpdateView.as_view(), name='delete')
    
]

