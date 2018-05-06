from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.RechargeLog)
admin.site.register(models.WorkoutRecord)
