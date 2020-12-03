
from rest_framework import serializers
# internal
from stok.models import Supplier, MaterialStock, Currency, BasicUnit


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ('id','name','phone','email','address')

class StockListSerialzer(serializers.ModelSerializer):
    supplier_name = serializers.ReadOnlyField(source="supplier.name")
    currency_code = serializers.ReadOnlyField(source="currency.code")
    basic_unit_code = serializers.ReadOnlyField(source="basic_unit.code")

    url = serializers.HyperlinkedIdentityField(view_name='api-stock-detail',
                                               lookup_field='pk')
                                               
    class Meta:
        model = MaterialStock
        fields = '__all__'

class StockCreateSerialzer(serializers.ModelSerializer):

    class Meta:
        model = MaterialStock
        fields = '__all__'

class SupplierCreateSerialzer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = '__all__'

# Angulara gidicek stock_name datası için ayarlanmıştı, şimdilik aksıya alındı.
# class StockNameListSerialzer(serializers.ModelSerializer):

#     class Meta:
#         model = MaterialStock
#         fields = ("id", "stock_name", "supplier")

class CurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Currency
        fields = '__all__'

class BasicUnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = BasicUnit
        fields = '__all__'