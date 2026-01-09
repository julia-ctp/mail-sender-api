from django.db import models

class ContactManager(models.Manager):
    def create_or_reactivate(self, user, **data):
        email = data.get('email')

        contact = self.filter(
            user=user,
            email=email,
            is_active=False
        ).first()

        if contact:
            for field, value in data.items():
                setattr(contact, field, value)
            contact.is_active = True
            contact.save()
            return contact

        return self.create(user=user, **data)
    