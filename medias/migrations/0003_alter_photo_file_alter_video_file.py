# Generated by Django 5.0.1 on 2024-02-13 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medias', '0002_alter_photo_experience_alter_photo_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.URLField(),
        ),
    ]