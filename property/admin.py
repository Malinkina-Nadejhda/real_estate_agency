from django.contrib import admin

from .models import Flat, Complaint, Owner

@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = (
        "town",
        "address",
        "owner_pure_phone",
    )
    readonly_fields = ("created_at",)
    list_filter = ("new_building",)
    raw_id_fields = ("liked_by",)
    list_display = (
        "address",
        "price",
        "new_building",
        "construction_year",
        "town",
        "owner_pure_phone",
    )
    list_editable = ("new_building",)


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ("user", "flat", )


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    search_fields = (
        "name",
        "owners_phonenumber",
        "owner_pure_phone",
    )
    list_display = (
        "name",
        "owners_phonenumber",
        "owner_pure_phone",
    )
    raw_id_fields = ("flats",)