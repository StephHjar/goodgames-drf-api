# Generated by Django 3.2.18 on 2023-03-02 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20230218_1536'),
        ('reviews', '0001_initial'),
        ('games', '0003_game_description'),
        ('comments', '0001_initial'),
        ('likes', '0003_auto_20230302_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='comment',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='comments.comment'),
        ),
        migrations.AlterField(
            model_name='like',
            name='game',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='games.game'),
        ),
        migrations.AlterField(
            model_name='like',
            name='post',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='posts.post'),
        ),
        migrations.AlterField(
            model_name='like',
            name='review',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='reviews.review'),
        ),
    ]
