# Generated by Django 5.0 on 2024-02-13 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equip_list', '0009_alter_machine_mainimage_alter_machineimages_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]