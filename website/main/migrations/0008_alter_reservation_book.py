# Generated by Django 4.2.7 on 2023-11-24 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0007_alter_reservation_book"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservation",
            name="book",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="main.books"
            ),
        ),
    ]