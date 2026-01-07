from django.db import models

class CampaignStatus(models.TextChoices):
    DRAFT = "draft"
    SENDING = "sending"
    SENT = "sent"
    FAILED = "failed"


class CampaignContactStatus(models.TextChoices):
    PENDING = "pending"
    SENT = "sent"
    FAILED = "failed"
    SKIPPED = "skipped"
