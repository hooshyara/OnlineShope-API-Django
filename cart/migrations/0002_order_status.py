# Generated by Django 4.2.5 on 2024-01-16 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('  ارسال شده', '  ارسال شده'), (' ارسال نشده', ' ارسال نشده'), ('  در انتظار ارسال ', '  در انتظار ارسال ')], default='در انتظار ارسال ', max_length=100),
        ),
    ]