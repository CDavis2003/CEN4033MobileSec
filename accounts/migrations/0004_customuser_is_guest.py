# Generated by Django 5.2 on 2025-04-22 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customuser_high_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_guest',
            field=models.BooleanField(default=False),
        ),
    ]
