from django.db import models
from django.contrib.auth.models import User
from dashboard.models import MemberCard

# Create your models here.


class RechargeLog(models.Model):
    Recharge_Methods = (
        ('WECHATPAY', 'WeChat Pay'),
        ('ALIPAY', 'Alipay'),
    )
    related_member_card = models.ForeignKey(MemberCard, on_delete=models.DO_NOTHING)
    quota = models.IntegerField(default=0)
    recharge_time = models.DateTimeField(auto_now_add=True)
    recharge_method = models.CharField(max_length=32, default='WECHATPAY', choices=Recharge_Methods)
    is_valid = models.BooleanField(default=False)

    class Meta:
        ordering = ['-recharge_time']

    def __str__(self):
        return self.related_member_card.related_user.username


class WorkoutRecord(models.Model):
    related_member_card = models.ForeignKey(MemberCard, on_delete=models.DO_NOTHING)
    check_in_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.related_member_card.related_user.username
