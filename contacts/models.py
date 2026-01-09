from django.db import models
from django.conf import settings
import uuid
from .managers import ContactManager


class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="contacts"
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    is_active = models.BooleanField(default=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ContactManager()

    class Meta:
        unique_together = ("user", "email")

    def __str__(self):
        return self.email
