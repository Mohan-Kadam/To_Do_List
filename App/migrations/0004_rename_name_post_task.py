# Generated by Django 4.0.5 on 2022-06-23 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_remove_post_note'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Name',
            new_name='Task',
        ),
    ]
