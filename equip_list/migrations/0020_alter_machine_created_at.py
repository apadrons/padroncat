# Generated by Django 5.0 on 2024-02-23 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equip_list', '0019_machine_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
