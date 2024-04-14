from django.contrib.auth.models import AbstractUser
from django.db import models
from .choices import INTEREST_CHOICES

import uuid


class User(AbstractUser):
    firstName = models.CharField(max_length=255, verbose_name='Имя')
    lastName = models.CharField(max_length=255, verbose_name='Фамилия')
    email = models.EmailField(unique=True, db_index=True)
    phoneNumber = models.CharField(
        verbose_name="Телефон",
        max_length=20,
    )
    interest = models.CharField(
        max_length=255,
        verbose_name='Интересы',
        choices=INTEREST_CHOICES,
        null=True,
        blank=True
    )

    notificationByTelegram = models.BooleanField(null=True,
                                                 blank=True)
    notificationByWhatsapp = models.BooleanField(null=True,
                                                 blank=True)
    notificationByVk = models.BooleanField(null=True,
                                           blank=True)
    notificationByViber = models.BooleanField(null=True,
                                              blank=True)

    telegram = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    whatsapp = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    vk = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    viber = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return self.get_full_name()

    def get_full_name(self) -> str:
        """ФИО."""
        names = [
            name
            for name in (self.last_name, self.first_name)
            if name is not None
        ]
        return " ".join(names)


class RecommendedActivities(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
        unique=True
    )
    event = models.ForeignKey(
        'events.Event',
        max_length=50,
        on_delete=models.CASCADE,
        related_name='events'

    )
    user = models.ForeignKey(
        'User',
        max_length=50,
        on_delete=models.CASCADE,
        related_name='user'
    )


class SelectedEvents(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
        unique=True
    )
    event = models.ForeignKey(
        'events.Event',
        max_length=50,
        on_delete=models.CASCADE,
        related_name='selected_events_events'

    )
    user = models.ForeignKey(
        'User',
        max_length=50,
        on_delete=models.CASCADE,
        related_name='selected_events_user'
    )


class UserActivities(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
        unique=True
    )
    event = models.ForeignKey(
        'events.Event',
        max_length=50,
        on_delete=models.CASCADE,
        related_name='user_activities_events'

    )
    user = models.ForeignKey(
        'User',
        max_length=50,
        on_delete=models.CASCADE,
        related_name='user_activities_user'
    )


class Notifications(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
        unique=True
    )
    event = models.ForeignKey(
        'UserActivities',
        max_length=50,
        on_delete=models.CASCADE,
        related_name='events'

    )
    user = models.ForeignKey(
        'User',
        max_length=50,
        on_delete=models.CASCADE,
        related_name='notifications_user'
    )
