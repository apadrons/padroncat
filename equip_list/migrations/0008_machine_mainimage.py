# Generated by Django 5.0 on 2024-02-13 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equip_list', '0007_remove_machine_image_machineimages'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='mainImage',
            field=models.ImageField(blank=True, default='boo.png', null=True, upload_to=''),
        ),
    ]
