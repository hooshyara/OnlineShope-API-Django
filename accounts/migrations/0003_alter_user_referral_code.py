# Generated by Django 4.2.5 on 2024-01-16 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_referral_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='referral_code',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
