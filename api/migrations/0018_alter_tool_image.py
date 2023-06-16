# Generated by Django 4.0.4 on 2023-05-10 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_remove_tool_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='image',
            field=models.URLField(help_text='link of the tool image', null=True, unique=True),
        ),
    ]
