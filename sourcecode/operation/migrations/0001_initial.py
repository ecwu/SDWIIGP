# Generated by Django 2.0.4 on 2018-05-06 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RechargeLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quota', models.IntegerField(default=0)),
                ('recharge_time', models.DateTimeField(auto_now_add=True)),
                ('recharge_method', models.CharField(choices=[('WECHATPAY', 'WeChat Pay'), ('ALIPAY', 'Alipay')], default='WECHATPAY', max_length=32)),
                ('related_member_card', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dashboard.MemberCard')),
                ('related_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]