# Generated by Django 4.1.4 on 2022-12-22 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gander', models.CharField(choices=[('M', 'Мужской'), ('F', 'Женский')], default='F', max_length=10, verbose_name='Пол')),
                ('Surname', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('Name', models.CharField(max_length=30, verbose_name='Имя')),
                ('Patronymic', models.CharField(max_length=40, verbose_name='Отчество')),
                ('DateOfBirth', models.DateField(auto_now_add=True)),
                ('Email', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Клиенты',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100, verbose_name='Название курса')),
                ('Goal', models.CharField(choices=[('P', 'Похудение, сушка, рельеф'), ('N', 'На всё тело'), ('R', 'Растяжка'), ('I', 'Интенсивы'), ('NA', 'Набор мышечной массы')], default='P', max_length=30, verbose_name='Цель занятий')),
                ('Place', models.CharField(choices=[('H', 'Дома'), ('Z', 'В зале')], default='H', max_length=10, verbose_name='Место занятий')),
                ('Description', models.TextField(max_length=3000, verbose_name='Описание')),
                ('Price', models.PositiveIntegerField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Курсы',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Surname', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('Name', models.CharField(max_length=30, verbose_name='Имя')),
                ('Patronymic', models.CharField(max_length=40, verbose_name='Отчество')),
                ('DateOfBirth', models.DateField(auto_now_add=True, verbose_name='Дата рождения')),
                ('Email', models.CharField(max_length=50, verbose_name='E-mail')),
                ('Post', models.CharField(max_length=40, verbose_name='Должность')),
                ('WorkExperience', models.CharField(max_length=10, verbose_name='Стаж работы')),
                ('Description', models.TextField(max_length=1000, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Сотрудники',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='TechnicalSupport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Surname', models.CharField(blank=True, max_length=30, verbose_name='Фамилия')),
                ('Name', models.CharField(blank=True, max_length=30, verbose_name='Имя')),
                ('Patronymic', models.CharField(blank=True, max_length=40, verbose_name='Отчество')),
                ('Post', models.CharField(max_length=40, verbose_name='Должность')),
                ('Description', models.TextField(max_length=2000, verbose_name='Описание')),
                ('Connection', models.CharField(choices=[('TE', 'Telegram'), ('WH', 'WhatsApp'), ('VI', 'Viber'), ('EM', 'E-mail')], default='TE', max_length=100, verbose_name='Связь')),
                ('Phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Техническая поддержка',
                'verbose_name_plural': 'Техническая поддержка',
            },
        ),
        migrations.CreateModel(
            name='TrainingSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateAndTime', models.DateTimeField(verbose_name='Дата и время')),
                ('CourseName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dreamfitdb.courses')),
                ('Staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dreamfitdb.staff')),
            ],
            options={
                'verbose_name': 'Расписание тренировок',
                'verbose_name_plural': 'Расписание тренировок',
            },
        ),
        migrations.CreateModel(
            name='Feedbacks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Feedback', models.TextField(max_length=1000, verbose_name='Отзыв')),
                ('Clients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dreamfitdb.clients')),
                ('CourseName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dreamfitdb.courses')),
            ],
            options={
                'verbose_name': 'Отзывы',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Feedback', models.TextField(blank=True, max_length=3000, verbose_name='Отзыв')),
                ('TechnicalSupport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dreamfitdb.technicalsupport')),
                ('TrainingSchedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dreamfitdb.trainingschedule')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dreamfitdb.clients')),
            ],
            options={
                'verbose_name': 'Личный кабинет',
                'verbose_name_plural': 'Личный кабинет',
            },
        ),
    ]
