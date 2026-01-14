from django.core.mail import send_mail
from email.utils import formataddr

def send_campaign_email(
    *,
    subject: str,
    body: str,
    from_email: str,
    from_name: str,
    to_email: str
):
    formatted_from = formataddr((from_name, from_email))

    send_mail(
        subject=subject,
        message=body,
        from_email=formatted_from,
        recipient_list=[to_email],
        fail_silently=False
    )
