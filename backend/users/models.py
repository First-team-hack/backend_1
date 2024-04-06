from django.contrib.auth.models import AbstractUser
from django.db import models

import uuid

class User(AbstractUser):
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    middle_name = models.CharField(max_length=255, verbose_name='Отчество')
    phone = models.CharField(
        verbose_name="Телефон",
        max_length=20,
    )
    email = models.EmailField(unique=True, db_index=True)
    post = models.CharField(
        max_length=255,
        verbose_name='Должность',
        null=True,
        blank=True
    )
    interests = models.CharField(
        max_length=255,
        verbose_name='Интересы',
        null=True,
        blank=True
    )
    def __str__(self) -> str:
        return self.get_full_name()

    def get_full_name(self) -> str:
        """ФИО."""
        names = [
            name
            for name in (self.last_name, self.first_name, self.middle_name)
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
        'Event',
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
        'Event',
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


class UserActivities(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
        unique=True
    )
    event = models.ForeignKey(
        'Event',
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
        related_name='user'
    )
