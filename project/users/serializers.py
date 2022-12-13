import datetime
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
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

    @extend_schema_field(OpenApiTypes.DECIMAL)
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


class UserStatisticsSerializer(serializers.Serializer):
    total_expenses = serializers.SerializerMethodField()
    total_income = serializers.SerializerMethodField()
    last_week_expenses = serializers.SerializerMethodField()
    last_week_income = serializers.SerializerMethodField()

    @property
    def expenses(self):
        return self.instance.transaction_set.filter(money_amount__lt=0)

    @property
    def income(self):
        return self.instance.transaction_set.filter(money_amount__gt=0)

    def aggregate_sum(self, queryset):
        return queryset.aggregate(sum_=Sum("money_amount"))["sum_"] or 0

    @extend_schema_field(OpenApiTypes.DECIMAL)
    def get_total_expenses(self, obj):
        return self.aggregate_sum(self.expenses)

    @extend_schema_field(OpenApiTypes.DECIMAL)
    def get_total_income(self, obj):
        return self.aggregate_sum(self.income)

    @extend_schema_field(OpenApiTypes.DECIMAL)
    def get_last_week_expenses(self, obj):
        return self.aggregate_sum(
            self.expenses.filter(
                datetime__gt=datetime.datetime.now() - datetime.timedelta(days=7),
            )
        )

    @extend_schema_field(OpenApiTypes.DECIMAL)
    def get_last_week_income(self, obj):
        return self.aggregate_sum(
            self.income.filter(
                datetime__gt=datetime.datetime.now() - datetime.timedelta(days=7),
            )
        )
