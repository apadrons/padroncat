# Generated by Django 5.0 on 2024-02-18 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equip_list', '0014_remove_machine_images_machineimages_machine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='price',
            field=models.IntegerField(),
        ),
    ]