from django.contrib import admin

from .models import User, PhotoCollection

@admin.register(PhotoCollection)
class PhotoCollectionAdmin(admin.ModelAdmin):
    list_display = ("id", "owner", "file")


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "last_name", "first_name"]
    search_fields = ["last_name"]
    list_filter = [
        "is_active",
        "is_staff",
        "is_superuser",
    ]
    fieldsets = (
        [None, {"fields": ["username", "password"]}],
        [
            ("Personal info"),
            {
                "fields": [
                    "last_name",
                    "first_name",
                ]
            },
        ],
        [
            ("Permissions"),
            {
                "fields": [
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ],
            },
        ],
        [("Important dates"), {"fields": ("last_login", "date_joined")}],
    )
    add_fieldsets = [
        [None, {"fields": ["username", "password1", "password2"]}],
        [
            ("Personal info"),
            {
                "fields": [
                    "last_name",
                    "first_name",
                ]
            },
        ],
        [
            ("Permissions"),
            {
                "fields": ["is_active", "is_staff", "is_superuser"],
            },
        ],
    ]
