from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_event', models.CharField(choices=[('online', 'онлайн'), ('offline', 'оффлайн')], max_length=50, verbose_name='Тип мероприятия')),
                ('street', models.CharField(max_length=255, verbose_name='Улица')),
                ('house_number', models.CharField(max_length=50, verbose_name='Номер дома')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
        migrations.CreateModel(
            name='Broadcast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_event', models.CharField(choices=[('online', 'онлайн'), ('offline', 'оффлайн')], max_length=50, verbose_name='Тип мероприятия')),
                ('file', models.FileField(upload_to='files/')),
            ],
            options={
                'verbose_name': 'Трансляция',
            },
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_event', models.CharField(choices=[('online', 'онлайн'), ('offline', 'оффлайн')], max_length=50, verbose_name='Тип мероприятия')),
                ('messages', models.CharField(max_length=255, verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Чат',
                'verbose_name_plural': 'Чаты',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название города')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_event', models.CharField(choices=[('online', 'онлайн'), ('offline', 'оффлайн')], max_length=50, verbose_name='Тип мероприятия')),
                ('question', models.CharField(max_length=255, verbose_name='Вопрос')),
                ('answer', models.CharField(max_length=255, verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'Опрос',
                'verbose_name_plural': 'Опросы',
            },
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('middle_name', models.CharField(max_length=255, verbose_name='Отчество')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True)),
                ('post', models.CharField(blank=True, max_length=255, null=True, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Спикер',
                'verbose_name_plural': 'Спикеры',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=255, verbose_name='Тема')),
                ('program', models.CharField(max_length=255, verbose_name='Программа')),
                ('type_event', models.CharField(choices=[('online', 'онлайн'), ('offline', 'оффлайн')], max_length=50, verbose_name='Тип мероприятия')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('date', models.DateField(verbose_name='дата')),
                ('time', models.TimeField(verbose_name='время')),
                ('status', models.CharField(choices=[('', ''), ('', '')], max_length=50, verbose_name='Статус мероприятия')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость')),
                ('adress', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event', to='events.adress', verbose_name='Адрес')),
                ('broadcast', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event', to='events.broadcast', verbose_name='Трансляция')),
                ('chat', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event', to='events.chat', verbose_name='Чат')),
                ('questionnaire', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event', to='events.questionnaire', verbose_name='Опрос')),
                ('speaker', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event_speaker', to='events.speaker', verbose_name='Спикер')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
        migrations.AddField(
            model_name='adress',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.city', verbose_name='Город'),
        ),
    ]
