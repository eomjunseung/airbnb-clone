# Generated by Django 2.2.5 on 2021-04-26 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_auto_20210423_1914'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='decription',
            new_name='description',
        ),
    ]