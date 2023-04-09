# Generated by Django 4.2 on 2023-04-09 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasktable',
            name='comment',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='tasktable',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/done/%Y/%m/%d/'),
        ),
    ]
