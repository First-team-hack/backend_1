from rest_framework import serializers

from users.models import User, UserActivities
from events.models import Event


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'middle_name',
            'email',
            'phone',
            'post',
            'interests'
        ]


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id',
            'topic',
            'program',
            'type_event',
            'name',
            'date',
            'time',
            'adress',
            'status',
            'speaker',
            'price'
        ]


# Пока сделан только чтоб в базу данные закидывать
class UserActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActivities
        fields = '__all__'
