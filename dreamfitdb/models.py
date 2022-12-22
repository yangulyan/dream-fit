from django.db import models


class Clients(models.Model):
    GANDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский')
    ]
    Gander = models.CharField('Пол', choices=GANDER_CHOICES, max_length=10, default='F')
    Surname = models.CharField('Фамилия', max_length=30)
    Name = models.CharField('Имя', max_length=30)
    Patronymic = models.CharField('Отчество', max_length=40)
    DateOfBirth = models.DateField(auto_now_add=True)
    Email = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.Surname} {self.Name} {self.Patronymic}'

    class Meta:
        verbose_name = 'Клиенты'
        verbose_name_plural = 'Клиенты'


class Courses(models.Model):
    GOAL_CHOICES = [
        ('P', 'Похудение, сушка, рельеф'),
        ('N', 'На всё тело'),
        ('R', 'Растяжка'),
        ('I', 'Интенсивы'),
        ('NA', 'Набор мышечной массы')
    ]
    PLACE_CHOICES = [
        ('H', 'Дома'),
        ('Z', 'В зале')
    ]
    Title = models.CharField('Название курса', max_length=100)
    Goal = models.CharField('Цель занятий', choices=GOAL_CHOICES, max_length=30, default='P')
    Place = models.CharField('Место занятий', choices=PLACE_CHOICES, max_length=10, default='H')
    Description = models.TextField('Описание', max_length=3000)
    Price = models.PositiveIntegerField('Цена')

    def __str__(self):
        return f'{self.Title}'

    class Meta:
        verbose_name = 'Курсы'
        verbose_name_plural = 'Курсы'


class Staff(models.Model):
    Surname = models.CharField('Фамилия', max_length=30)
    Name = models.CharField('Имя', max_length=30)
    Patronymic = models.CharField('Отчество', max_length=40)
    DateOfBirth = models.DateField('Дата рождения', auto_now_add=True)
    Email = models.CharField('E-mail', max_length=50)
    Post = models.CharField('Должность', max_length=40)
    WorkExperience = models.CharField('Стаж работы', max_length=10)
    Description = models.TextField('Описание', max_length=1000)

    def __str__(self):
        return f'{self.Surname} {self.Name} {self.Patronymic}'

    class Meta:
        verbose_name = 'Сотрудники'
        verbose_name_plural = 'Сотрудники'


class Feedbacks(models.Model):
    Clients = models.ForeignKey('Clients', on_delete=models.CASCADE)
    Feedback = models.TextField('Отзыв', max_length=1000)
    CourseName = models.ForeignKey('Courses', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Feedback}'

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'


class TechnicalSupport(models.Model):
    CONNECTION_CHOICES = [
        ('TE', 'Telegram'),
        ('WH', 'WhatsApp'),
        ('VI', 'Viber'),
        ('EM', 'E-mail')
    ]
    Surname = models.CharField('Фамилия', max_length=30, blank=True)
    Name = models.CharField('Имя', max_length=30, blank=True)
    Patronymic = models.CharField('Отчество', max_length=40, blank=True)
    Post = models.CharField('Должность', max_length=40)
    Description = models.TextField('Описание', max_length=2000)
    Connection = models.CharField('Связь', choices=CONNECTION_CHOICES, max_length=100, default='TE')
    Phone = models.CharField('Номер телефона', max_length=20)

    def __str__(self):
        return f'{self.Post}'

    class Meta:
        verbose_name = 'Техническая поддержка'
        verbose_name_plural = 'Техническая поддержка'


class Account(models.Model):
    User = models.ForeignKey('Clients', on_delete=models.CASCADE)
    TrainingSchedule = models.ForeignKey('TrainingSchedule', on_delete=models.CASCADE)
    TechnicalSupport = models.ForeignKey('TechnicalSupport', on_delete=models.CASCADE)
    Feedback = models.TextField('Отзыв', max_length=3000, blank=True)

    def __str__(self):
        return f'{self.User}'

    class Meta:
        verbose_name = 'Личный кабинет'
        verbose_name_plural = 'Личный кабинет'


class TrainingSchedule(models.Model):
    Staff = models.ForeignKey('Staff', on_delete=models.CASCADE)
    CourseName = models.ForeignKey('Courses', on_delete=models.CASCADE)
    DateAndTime = models.DateTimeField('Дата и время')

    def __str__(self):
        return f'{self.CourseName}'

    class Meta:
        verbose_name = 'Расписание тренировок'
        verbose_name_plural = 'Расписание тренировок'
