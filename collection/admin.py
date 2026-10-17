
from django.contrib import admin
from .models import Collections


@admin.register(Collections)
class CollectionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "user",
        "created_at",
        "updated_at",
    )

    search_fields = ("name", "description", "user__username")

    list_filter = ("created_at", "updated_at")

    ordering = ("-created_at",)
