# Generated by Django 4.0.4 on 2023-05-11 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_alter_tool_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='related_projects',
            field=models.ManyToManyField(blank=True, help_text='related projects', to='api.project'),
        ),
    ]
