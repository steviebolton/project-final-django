# Generated by Django 2.0.6 on 2018-08-29 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0008_order_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='town_or_city',
            new_name='city',
        ),
    ]
