# Generated by Django 3.2.6 on 2021-08-30 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tsmapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tsm',
            old_name='Text',
            new_name='text',
        ),
    ]