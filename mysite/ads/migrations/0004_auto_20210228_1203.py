# Generated by Django 3.1.4 on 2021-02-28 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ads', '0003_auto_20210228_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ads_owned', to=settings.AUTH_USER_MODEL),
        ),
    ]