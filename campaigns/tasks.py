from celery import shared_task
from .models import Campaign, CampaignContact
from .enums import CampaignContactStatus, CampaignStatus
from .services.email_service import send_campaign_email

@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=5, retry_kwargs={"max_retries": 3})
def send_campaign_task(self, campaign_id): 
    campaign = Campaign.objects.get(pk=campaign_id)

    campaign_contacts = CampaignContact.objects.select_related(
        "contact"
    ).filter(
        campaign=campaign,
        status=CampaignContactStatus.PENDING
    ) 

    for campaign_contact in campaign_contacts: 
        try:
            send_campaign_email(
                subject=campaign.subject,
                body=campaign.body,
                from_email=campaign.sender_email,
                from_name=campaign.sender_name,
                to_email=campaign_contact.contact.email
            )

            campaign_contact.status = CampaignContactStatus.SENT
            campaign_contact.save()

        except Exception as e:
            campaign_contact.status = CampaignContactStatus.FAILED
            campaign_contact.error_message = str(e)
            campaign_contact.save()
            continue

    campaign.status = CampaignStatus.SENT
    campaign.save()


