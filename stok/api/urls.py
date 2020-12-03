from django.urls import path
# internal
from stok.api.routes import SupplierList, StockList, StockDetail, CurrencyList, BasicUnitList, SupplierDetail

# Angulara gidicek stock_name datası için ayarlanmıştı, şimdilik aksıya alındı.
# from stok.api.routes import StockNameList

urlpatterns = [
    path('suppliers/', SupplierList.as_view(), name='api-supplier-list'),
    path('suppliers/<int:pk>', SupplierDetail.as_view(), name='api-supplier-detail'),
    path('stocks/', StockList.as_view(), name='api-stock-list'),
    path('stocks/<int:pk>', StockDetail.as_view(), name='api-stock-detail'),        
    path('currencies/', CurrencyList.as_view(), name='currency-list'),        
    path('basicunits/', BasicUnitList.as_view(), name='basic-unit-list')

     # Angulara gidicek stock_name datası için ayarlanmıştı, şimdilik aksıya alındı.        
     # path('stock-names/', StockNameList.as_view(), name='api-stock-list')
]