from django.db import models

from .choices import TYPES_CHOICES, STATUS_CHOICES


class Speaker(models.Model):
    ''' Модель спикера '''

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
        blank=True,
    )

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        names = [
            name
            for name in (self.last_name, self.first_name, self.middle_name)
            if name is not None
        ]
        return " ".join(names)

    class Meta:
        verbose_name = 'Спикер'
        verbose_name_plural = 'Спикеры'


class Questionnaire(models.Model):
    ''' Модель опроса '''

    type_event = models.CharField(
        max_length=50,
        choices=TYPES_CHOICES,
        verbose_name='Тип мероприятия',
    )
    question = models.CharField(
        max_length=255,
        verbose_name='Вопрос',
    )
    answer = models.CharField(
        max_length=255,
        verbose_name='Ответ',
    )

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Chat(models.Model):
    ''' Модель чата '''

    type_event = models.CharField(
        max_length=50,
        choices=TYPES_CHOICES,
        verbose_name='Тип мероприятия',
    )
    messages = models.CharField(
        max_length=255,
        verbose_name='Сообщение',
    )

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'


class Broadcast(models.Model):
    ''' Модель трансляции '''

    type_event = models.CharField(
        max_length=50,
        choices=TYPES_CHOICES,
        verbose_name='Тип мероприятия',
    )
    file = models.FileField(upload_to='files/')

    class Meta:
        verbose_name = 'Трансляция'


class City(models.Model):
    """ Модель для названий городов """

    name = models.CharField(max_length=255, verbose_name='Название города')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Adress(models.Model):
    ''' Модель адреса '''

    type_event = models.CharField(
        max_length=50,
        choices=TYPES_CHOICES,
        verbose_name='Тип мероприятия',
    )
    city = models.ForeignKey(
        City, on_delete=models.SET_NULL, null=True, verbose_name='Город'
    )
    street = models.CharField(max_length=255, verbose_name='Улица')
    house_number = models.CharField(max_length=50, verbose_name='Номер дома')

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class Event(models.Model):
    ''' Модель мероприятия '''

    topic = models.CharField(
        max_length=255,
        verbose_name='Тема',
    )
    program = models.CharField(
        max_length=255,
        verbose_name='Программа',
    )
    type_event = models.CharField(
        max_length=50,
        choices=TYPES_CHOICES,
        verbose_name='Тип мероприятия',
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Название',
    )
    date = models.DateField(
        verbose_name='дата',
        blank=False,
        null=False,
    )
    time = models.TimeField(
        verbose_name='время',
        blank=False,
        null=False,
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        verbose_name='Статус мероприятия',
    )
    speaker = models.OneToOneField(
        Speaker,
        on_delete=models.SET_NULL,
        null=True,
        related_name='event',
        verbose_name='Спикер',
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Стоимость',
    )
    questionnaire = models.OneToOneField(
        Questionnaire,
        on_delete=models.SET_NULL,
        null=True,
        related_name='event',
        verbose_name='Опрос',
    )
    chat = models.OneToOneField(
        Chat,
        on_delete=models.SET_NULL,
        null=True,
        related_name='event',
        verbose_name='Чат',
    )
    broadcast = models.OneToOneField(
        Broadcast,
        on_delete=models.SET_NULL,
        null=True,
        related_name='event',
        verbose_name='Трансляция',
    )
    adress = models.ForeignKey(
        Adress,
        on_delete=models.SET_NULL,
        null=True,
        related_name='event',
        verbose_name='Адрес',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
