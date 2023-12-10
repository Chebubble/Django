from rest_framework import serializers
<<<<<<< HEAD

from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
=======
from logistic.models import Product, Stock, StockProduct

class ProductSerializer(serializers.ModelSerializer):
    # настройте сериализатор для продукта
      class Meta:
>>>>>>> da34ece7ad16c6ca2ff424630ef67e03ef525b02
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    # настройте сериализатор для позиции продукта на складе
    class Meta:
        model = StockProduct
        fields = [
            'product',
            'quantity',
            'price',
        ]


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    # настройте сериализатор для склада
    class Meta:
        model = Stock
        fields = [
            'id',
            'address',
            'positions',
        ]

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)
        
        for position in positions:
            StockProduct.objects.create(
                stock=stock,
                product=position['product'],
                quantity=position['quantity'],
                price=position['price'],
            )

        for position in positions:
            StockProduct.objects.create(
                stock=stock,
                product=position['product'],
                quantity=position['quantity'],
                price=position['price'],
            )

        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)

        for position in positions:
            StockProduct.objects.update_or_create(
                stock=stock,
                product=position['product'],
                defaults={
                    'quantity': position['quantity'],
                    'price': position['price'],
                }
            )
<<<<<<< HEAD
=======

        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions
>>>>>>> da34ece7ad16c6ca2ff424630ef67e03ef525b02

        return stock