# Generated by Django 3.2.6 on 2021-08-30 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsmapp', '0002_rename_text_tsm_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tsm',
            name='email',
            field=models.EmailField(max_length=30),
        ),
        migrations.AlterField(
            model_name='tsm',
            name='phone',
            field=models.CharField(max_length=13),
        ),
    ]
