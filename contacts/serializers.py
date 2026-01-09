from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            "id", 
            "name", 
            "email", 
            "is_active", 
            "created_at", 
            "updated_at"
        )
        read_only_fields = ("id", "is_active", "created_at", "updated_at")

    def validate_email(self, email):
        user = self.context["request"].user

        contact = Contact.objects.filter(
            user=user,
            email=email,
            is_active=True
        )

        if self.instance:
            contact = contact.exclude(id=self.instance.id)

        if contact.exists():
            raise serializers.ValidationError(
                "This email already exists for this user."
            )

        return email
