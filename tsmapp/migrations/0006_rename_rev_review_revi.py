# Generated by Django 3.2.6 on 2021-08-31 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tsmapp', '0005_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='rev',
            new_name='revi',
        ),
    ]
