from rest_framework import serializers

from logistic.models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    # настройте сериализатор для склада
    class Meta:
        model = Stock
        fields = ['address', 'positions']

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        # print(positions)

        # создаем склад по его параметрам
        stock = super().create(validated_data)

        # здесь вам надо заполнить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions
        for position in positions:
            position.update({'stock': stock})
            # print(position)
            sp = StockProduct(**position)
            sp.save()
            # StockProduct().objects.create(position)

        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)

        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions
        for position in positions:
            position.update({'stock': stock})
            # for stock_product in StockProduct.objects.all():
            #     # StockProduct.objects.update()
            #     if stock_product.product == position['product']:
            #         stock_product.quantity = position['quantity']
            #         stock_product.price = position['price']
            stock_product = StockProduct.objects.get(product=position['product'])
            stock_product.quantity = position['quantity']
            stock_product.price = position['price']
            stock_product.save()

        return stock
