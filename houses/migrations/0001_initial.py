# Generated by Django 5.0.1 on 2024-01-30 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('price_per_night', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=140)),
                ('pets_allowed', models.BooleanField(default=False)),
            ],
        ),
    ]
