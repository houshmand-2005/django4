# Generated by Django 4.0.4 on 2022-05-14 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_roadmaps_delete_roadmap'),
    ]

    operations = [
        migrations.CreateModel(
            name='films',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=300)),
                ('tpicofmove', models.CharField(max_length=200)),
                ('namemove', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='roadmaps',
            name='namemove',
        ),
        migrations.RemoveField(
            model_name='roadmaps',
            name='url',
        ),
    ]
