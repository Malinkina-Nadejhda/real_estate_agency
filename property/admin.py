from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flats.through
    extra = 3
    raw_id_fields = ("owner",)


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = (
        "town",
        "address",
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
    )
    list_editable = ("new_building",)
    inlines = (OwnerInline,)


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ("user", "flat",)


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
