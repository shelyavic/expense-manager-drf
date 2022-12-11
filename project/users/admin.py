from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        (
            None,
            {
                "fields": (
                    (
                        "email",
                        "password",
                    )
                ),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = ((None, {"fields": ("email", "password1", "password2")}),)

    ordering = ("email",)

    list_display = ("email", "is_staff")


admin.site.register(CustomUser, CustomUserAdmin)
