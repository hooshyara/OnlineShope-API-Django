# Generated by Django 4.2.5 on 2024-01-22 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='Cooperation_percentage',
            field=models.PositiveBigIntegerField(null=True),
        ),
    ]
