# Generated by Django 5.0 on 2024-02-17 00:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equip_list', '0012_alter_machineimages_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machineimages',
            name='machine',
        ),
        migrations.AddField(
            model_name='machine',
            name='images',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='equip_list.machineimages'),
            preserve_default=False,
        ),
    ]