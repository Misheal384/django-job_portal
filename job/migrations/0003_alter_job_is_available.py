# Generated by Django 5.0.1 on 2024-04-03 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_alter_job_is_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='is_available',
            field=models.BooleanField(default=False),
        ),
    ]
