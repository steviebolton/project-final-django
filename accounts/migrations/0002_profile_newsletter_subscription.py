# Generated by Django 2.0.6 on 2018-08-28 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='newsletter_subscription',
            field=models.BooleanField(default=True),
        ),
    ]
