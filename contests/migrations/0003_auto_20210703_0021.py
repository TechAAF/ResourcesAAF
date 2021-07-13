# Generated by Django 3.2.5 on 2021-07-02 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0002_auto_20210703_0008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='contest',
            name='category',
            field=models.ManyToManyField(null=True, to='contests.Category'),
        ),
    ]
