from django.contrib import admin
from .models import Profile, Level


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ("id", "level", "second_level")
    list_filter = ("level", "second_level")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "pfadi_name", "level", "visible")
    list_filter = ("level", "visible")
    search_fields = (
        "name",
        "second_name",
        "last_name",
        "pfadi_name",
        "phone_number",
        "email",
    )
