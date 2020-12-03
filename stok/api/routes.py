from rest_framework import generics

#internal
from stok.models import Supplier, MaterialStock, Currency, BasicUnit
from stok.api.serializers import (SupplierSerializer, StockListSerialzer,StockCreateSerialzer, SupplierCreateSerialzer, CurrencySerializer, BasicUnitSerializer)

# Angulara gidicek stock_name datası için ayarlanmıştı, şimdilik aksıya alındı.
# from stok.api.serializers import StockNameListSerialzer

# class StockNameList(generics.ListAPIView):
#     queryset = MaterialStock.objects.all()
#     def get_serializer_class(self):
#         return StockNameListSerialzer


class SupplierList(generics.ListCreateAPIView):
    serializer_class = SupplierSerializer

    def get_queryset(self):
        queryset = Supplier.objects.all()
        paramSupplierName = self.request.query_params.get('name')
        if paramSupplierName:
            queryset = queryset.filter(name__icontains=paramSupplierName)
        return queryset

class StockList(generics.ListCreateAPIView):
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return StockCreateSerialzer
        return StockListSerialzer

    def get_queryset(self):
        queryset = MaterialStock.objects.all()
        paramStockName = self.request.query_params.get('name')
        if paramStockName:
            queryset = queryset.filter(stock_name__icontains=paramStockName)
            # queryset = queryset.filter(stock_name__istartswith=paramStockName)
        return queryset
        
class StockDetail(generics.RetrieveUpdateAPIView):
    queryset = MaterialStock.objects.all()

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return StockCreateSerialzer
        return StockListSerialzer

class SupplierDetail(generics.RetrieveUpdateAPIView):
    queryset = Supplier.objects.all()

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return SupplierCreateSerialzer
        return SupplierSerializer

class CurrencyList(generics.ListCreateAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

class BasicUnitList(generics.ListCreateAPIView):
    queryset = BasicUnit.objects.all()
    serializer_class = BasicUnitSerializer