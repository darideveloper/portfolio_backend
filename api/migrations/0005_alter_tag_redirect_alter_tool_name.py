# Generated by Django 4.0.4 on 2023-03-28 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_tool_redirect_alter_contact_image_alter_tag_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='redirect',
            field=models.URLField(blank=True, help_text='link where the tag redirects'),
        ),
        migrations.AlterField(
            model_name='tool',
            name='name',
            field=models.CharField(help_text='tool name', max_length=50),
        ),
    ]