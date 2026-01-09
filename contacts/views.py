from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Contact
from .serializers import ContactSerializer


class ContactViewSet(ModelViewSet):
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user, is_active=True)

    def perform_create(self, serializer):
        contact = Contact.objects.create_or_reactivate(
            user=self.request.user,
            **serializer.validated_data
        )
        serializer.instance = contact

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

