# Generated by Django 4.0.5 on 2022-06-23 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_alter_post_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Complete',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Incomplete',
            field=models.BooleanField(default=False),
        ),
    ]
