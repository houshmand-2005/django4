# Generated by Django 4.0.4 on 2022-05-14 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_alter_films_urlofmove'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='urlofmove',
            field=models.URLField(max_length=300),
        ),
    ]