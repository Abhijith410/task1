# Generated by Django 4.1.3 on 2023-05-01 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0010_alter_blog_doc_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="content",
            field=models.TextField(db_column="content", max_length=500),
        ),
        migrations.AlterField(
            model_name="blog",
            name="summary",
            field=models.TextField(db_column="sum", max_length=50),
        ),
    ]
