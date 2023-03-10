# Generated by Django 3.2.18 on 2023-03-04 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20230218_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='completed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='currently_playing',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
