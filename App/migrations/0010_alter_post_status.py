# Generated by Django 4.0.5 on 2022-06-29 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_alter_post_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Status',
            field=models.CharField(max_length=2),
        ),
    ]
