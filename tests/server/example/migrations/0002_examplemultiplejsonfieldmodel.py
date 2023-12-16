from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("example", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExampleMultipleJsonFieldModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("my_json1", models.JSONField()),
                ("my_json2", models.JSONField()),
                ("my_json3", models.JSONField()),
            ],
        ),
    ]
