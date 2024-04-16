from django.contrib import admin

from .models import (
    Adress,
    Broadcast,
    Chat,
    City,
    Event,
    Favorite,
    Questionnaire,
    Speaker,
)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):

    list_display = ('name',)


@admin.register(Adress)
class AdressAdmin(admin.ModelAdmin):

    list_display = (
        'type_event',
        'city',
        'street',
        'house_number',
    )


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):

    list_display = (
        'first_name',
        'last_name',
        'middle_name',
        'phone',
        'email',
        'post',
    )


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    pass


@admin.register(Broadcast)
class BroadcastAdmin(admin.ModelAdmin):

    list_display = ('type_event',)


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    pass


@admin.register(Questionnaire)
class Questionnaire(admin.ModelAdmin):

    list_display = (
        'type_event',
        'question',
        'answer',
    )


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'themes',
        'format',
        'title',
        'date',
        'time',
        'status',
        'speakerDescription',
        'seatsLeft',
    )
