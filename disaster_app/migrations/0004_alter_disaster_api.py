# Generated by Django 4.1.7 on 2023-03-07 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disaster_app', '0003_rename_original_api_disaster_api'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disaster',
            name='api',
            field=models.CharField(choices=[('Manual', 'Manually Added'), ('EONET', 'EONET'), ('ReliefWeb', 'ReliefWeb')], default=None, max_length=30),
        ),
    ]
