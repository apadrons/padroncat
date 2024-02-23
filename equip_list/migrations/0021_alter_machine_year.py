# Generated by Django 5.0 on 2024-02-23 03:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equip_list', '0020_alter_machine_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='year',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(2024), django.core.validators.MinValueValidator(1960)]),
        ),
    ]
