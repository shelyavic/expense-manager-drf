from rest_framework import serializers
from api.models import Category, Transaction

class LowercaseCharField(serializers.CharField):
    def to_internal_value(self, data):
        value = super().to_internal_value(data)
        return value.lower()


class CategorySerializer(serializers.ModelSerializer):
    name = LowercaseCharField(max_length=255)
    
    class Meta:
        model = Category
        fields = ["id", "name"]
        extra_kwargs = {"id": {"read_only": True}}



class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"
        extra_kwargs = {"owner": {"read_only": True}}