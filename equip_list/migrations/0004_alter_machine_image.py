# Generated by Django 5.0 on 2024-02-11 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equip_list', '0003_machine_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='image',
            field=models.ImageField(blank=True, default='padroncat\\media\\machine_images\\machine1.JPG', null=True, upload_to='machine_images'),
        ),
    ]
