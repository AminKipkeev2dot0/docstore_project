# Generated by Django 3.1.5 on 2022-12-08 08:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('personal_account', '0005_auto_20221115_0309'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='user',
            field=models.ForeignKey(default=-18735, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
