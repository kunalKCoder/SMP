# Generated by Django 3.2 on 2021-05-06 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0002_contact_desc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='desc',
            new_name='message',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='mobile',
        ),
    ]
