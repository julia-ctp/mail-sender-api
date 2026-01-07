from django.contrib import admin
from .models import Campaign, CampaignContact

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ("sender_email", "subject", "status", "created_at")

@admin.register(CampaignContact)
class CampaignContactAdmin(admin.ModelAdmin):
    list_display = ("campaign", "contact", "created_at", "status")
