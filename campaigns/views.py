from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Campaign, CampaignContact
from contacts.models import Contact
from .serializers import CampaignSerializer
from .enums import CampaignStatus, CampaignContactStatus
from .tasks import send_campaign_task
from core.pagination import CustomCursorPagination


class CampaignViewset(ModelViewSet):
    serializer_class = CampaignSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomCursorPagination

    def get_queryset(self):
        return Campaign.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user, 
            sender_email=self.request.user.email
        )

    @action(detail=True, methods=["post"])
    def send(self, request, pk=None):
        campaign = self.get_object()

        if campaign.status in (
            CampaignStatus.SENT,
            CampaignStatus.SENDING
        ):
            return Response(
                {"detail": "This campaign has already been sent"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        campaign.status = CampaignStatus.SENDING
        campaign.save() 

        contacts = Contact.objects.filter(
            user=request.user, is_active=True  
        )

        for contact in contacts:
            CampaignContact.objects.create(
                campaign=campaign, 
                contact=contact, 
                status=CampaignContactStatus.PENDING
            )

        send_campaign_task.delay_on_commit(str(campaign.id)) 

        return Response(
            {"detail": "Campaign is being sent"},
            status=status.HTTP_202_ACCEPTED,
        )
