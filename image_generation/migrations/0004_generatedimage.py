# Generated by Django 4.2.3 on 2023-07-04 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("image_generation", "0003_delete_imagegeneration"),
    ]

    operations = [
        migrations.CreateModel(
            name="GeneratedImage",
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
                ("text", models.TextField()),
                ("date_added", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
