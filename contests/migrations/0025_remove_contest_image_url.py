# Generated by Django 3.2.3 on 2021-07-24 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0024_auto_20210724_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contest',
            name='image_url',
        ),
    ]
