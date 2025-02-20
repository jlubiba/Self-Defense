# Generated by Django 5.1.6 on 2025-02-20 08:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tutorials", "0005_remove_videotutorial_url_videotutorial_iframe_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="videotutorial",
            name="likes",
            field=models.ManyToManyField(
                related_name="video_likes", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="videotutorial",
            name="subcategory",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="videos",
                to="tutorials.subcategory",
            ),
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("body", models.TextField(verbose_name="Comment...")),
                ("post_date", models.DateTimeField(auto_now_add=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "video",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="tutorials.videotutorial",
                    ),
                ),
            ],
        ),
    ]
