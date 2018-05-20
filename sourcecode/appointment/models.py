from django.db import models
from django.contrib.auth.models import User
from dashboard.models import MemberCard
# Create your models here.


class Appointment(models.Model):
    appointer = models.ForeignKey(MemberCard, on_delete=models.DO_NOTHING)
    appointee = models.ForeignKey(User, limit_choices_to={'groups__name': "coach"}, on_delete=models.DO_NOTHING)
    appoint_time_date = models.DateField()
    appoint_time_hour = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-appoint_time_date', 'appoint_time_hour']

    def __str__(self):
        return str(self.id)
