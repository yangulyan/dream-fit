from django.contrib import admin

from dreamfitdb.models import Clients, Courses, Staff, Feedbacks, TechnicalSupport, Account, TrainingSchedule


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    pass


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    pass


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    pass


@admin.register(Feedbacks)
class FeedbacksAdmin(admin.ModelAdmin):
    pass


@admin.register(TechnicalSupport)
class TechnicalSupportAdmin(admin.ModelAdmin):
    pass


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass


@admin.register(TrainingSchedule)
class TrainingScheduleAdmin(admin.ModelAdmin):
    pass
