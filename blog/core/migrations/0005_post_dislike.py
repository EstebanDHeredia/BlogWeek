# Generated by Django 4.2.11 on 2024-05-27 21:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0004_post_likes"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="dislike",
            field=models.ManyToManyField(
                to=settings.AUTH_USER_MODEL, verbose_name="No me gusta"
            ),
        ),
    ]
