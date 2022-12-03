from rest_framework import serializers
from users.models import CustomUser
from django.contrib.auth.password_validation import validate_password
from django.db.models import Sum


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)
    balance = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ("id", "email", "balance", "password", "password2")
        extra_kwargs = {"id": {"read_only": True}}

    def get_balance(self, obj):
        result = obj.transaction_set.aggregate(transactions_sum=Sum("money_amount"))
        return result["transactions_sum"] or 0

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError(
                {
                    "password": "Password fields didn't match.",
                    "password2": "Password fields didn't match.",
                }
            )
        return data

    def create(self, validated_data):
        user = CustomUser.objects.create(email=validated_data["email"])
        user.set_password(validated_data["password"])
        user.save()
        return user
