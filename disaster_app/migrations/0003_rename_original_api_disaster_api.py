# Generated by Django 4.1.7 on 2023-03-07 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disaster_app', '0002_alter_disaster_reference_alter_disaster_source'),
    ]

    operations = [
        migrations.RenameField(
            model_name='disaster',
            old_name='original_api',
            new_name='api',
        ),
    ]
