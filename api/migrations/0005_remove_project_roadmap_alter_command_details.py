# Generated by Django 4.0.4 on 2023-03-14 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_project_roadmap_alter_badge_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='roadmap',
        ),
        migrations.AlterField(
            model_name='command',
            name='details',
            field=models.TextField(null=True),
        ),
    ]