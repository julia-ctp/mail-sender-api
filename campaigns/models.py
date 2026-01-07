from django.db import models
from django.conf import settings
from contacts.models import Contact
from .enums import CampaignStatus, CampaignContactStatus
import uuid


class Campaign(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="campaigns"
    )
    subject = models.CharField(max_length=60)
    body = models.TextField()
    sender_name = models.CharField(max_length=50)
    sender_email = models.EmailField()
    status = models.CharField(
        max_length=20, choices=CampaignStatus.choices, default=CampaignStatus.DRAFT
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.subject


class CampaignContact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    campaign = models.ForeignKey(
        Campaign, on_delete=models.CASCADE, related_name="campaign_contacts"
    )
    contact = models.ForeignKey(
        Contact, on_delete=models.CASCADE, related_name="campaign_contacts"
    )
    status = models.CharField(
        max_length=20,
        choices=CampaignContactStatus.choices,
        default=CampaignContactStatus.PENDING,
    )
    error_message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("campaign", "contact")
