# Generated by Django 2.2.9 on 2021-12-25 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20211221_1924'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='descrption',
            new_name='description',
        ),
    ]
