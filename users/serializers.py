from rest_framework import serializers
from users.models import CustomUser
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ("id", "email", "password", "password2")
        extra_kwargs = {"id": {"read_only": True}}

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
        user = CustomUser.objects.create_user(
            validated_data["email"], validated_data["password"]
        )
        return user
