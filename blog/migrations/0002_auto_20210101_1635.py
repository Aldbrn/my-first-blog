# Generated by Django 3.1.3 on 2021-01-01 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='test',
            new_name='text',
        ),
    ]
