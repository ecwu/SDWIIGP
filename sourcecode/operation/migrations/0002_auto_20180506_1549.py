# Generated by Django 2.0.4 on 2018-05-06 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkoutRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recharge_time', models.DateTimeField(auto_now_add=True)),
                ('related_member_card', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dashboard.MemberCard')),
            ],
        ),
        migrations.RemoveField(
            model_name='rechargelog',
            name='related_user',
        ),
    ]
