# Generated by Django 3.2.3 on 2021-06-05 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_alter_addphoto_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Addphoto',
            new_name='Photo',
        ),
    ]
