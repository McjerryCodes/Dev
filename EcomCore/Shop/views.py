from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class ProductPagination(PageNumberPagination):
    page_size = 10  # Number of products per page
    page_size_query_param = 'page_size'
    max_page_size = 100

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'room', openapi.IN_QUERY, description="Filter by room name", type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'concept', openapi.IN_QUERY, description="Filter by concept name", type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'price_min', openapi.IN_QUERY, description="Minimum price", type=openapi.TYPE_NUMBER
            ),
            openapi.Parameter(
                'price_max', openapi.IN_QUERY, description="Maximum price", type=openapi.TYPE_NUMBER
            ),
        ]
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Product.objects.all()
        room = self.request.query_params.get('room', None)
        concept = self.request.query_params.get('concept', None)
        price_min = self.request.query_params.get('price_min', None)
        price_max = self.request.query_params.get('price_max', None)

        if room:
            queryset = queryset.filter(room__name=room)
        if concept:
            queryset = queryset.filter(concept__name=concept)
        if price_min:
            queryset = queryset.filter(price__gte=price_min)
        if price_max:
            queryset = queryset.filter(price__lte=price_max)

        return queryset
    
class ProductRetrieveDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Product.objects.all
        serializer_class = ProductSerializer
        permission_classes = AllowAny

        def delete (self, serializer,pk):
            serializer.save(author=self.request.user)