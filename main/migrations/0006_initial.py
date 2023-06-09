# Generated by Django 4.1.3 on 2023-04-26 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("main", "0005_delete_registration"),
    ]

    operations = [
        migrations.CreateModel(
            name="Registration",
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
                ("usertype", models.CharField(max_length=20)),
                ("firstname", models.CharField(db_column="fname", max_length=20)),
                ("lastname", models.CharField(db_column="lname", max_length=20)),
                ("email", models.TextField(db_column="email", max_length=20)),
                ("address", models.TextField(db_column="address", max_length=50)),
                ("username", models.CharField(db_column="usname", max_length=20)),
                ("password", models.CharField(db_column="pswd", max_length=20)),
                ("confpassword", models.CharField(db_column="cnfpass", max_length=20)),
                ("image", models.ImageField(upload_to="images/")),
            ],
            options={
                "db_table": "registration",
            },
        ),
    ]
