# Generated by Django 4.0.1 on 2022-01-21 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='done',
            new_name='completed',
        ),
    ]
