# Generated by Django 2.0.4 on 2018-05-06 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0002_auto_20180506_1549'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rechargelog',
            options={'ordering': ['-recharge_time']},
        ),
        migrations.AddField(
            model_name='rechargelog',
            name='is_valid',
            field=models.BooleanField(default=False),
        ),
    ]
