from rest_framework import serializers
from .models import Campaign, CampaignContact
from .enums import CampaignStatus

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = (
            "id", 
            "subject", 
            "body",
            "sender_name", 
            "sender_email",
            "status", 
            "created_at", 
            "updated_at"
        )
        read_only_fields = (
            "id",
            "sender_email", 
            "status", 
            "created_at", 
            "updated_at"
        )

    def validate(self, attrs): 
        if self.instance: 
            if self.instance.status in [
                CampaignStatus.SENT, 
                CampaignStatus.SENDING
            ]:
                raise serializers.ValidationError(
                    "This campaign cannot be edited."
                )
            
        return attrs   


class CampaignContactSerializer(serializers.ModelSerializer):
    contact_name = serializers.CharField(source="contact.name")
    contact_email = serializers.CharField(source="contact.email")

    class Meta:
        model = CampaignContact
        fields = (
            "id", 
            "contact_name",
            "contact_email",
            "status", 
            "error_message",
            "created_at"
        )
        read_only_fields = fields
