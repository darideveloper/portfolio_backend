# Generated by Django 4.0.4 on 2023-03-13 23:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_user_badges_user_web_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80, unique=True)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('last_update', models.DateField(default=django.utils.timezone.now)),
                ('logo', models.FileField(null=True, upload_to='project_logos')),
                ('desciption', models.TextField()),
                ('details', models.TextField()),
                ('clone_repo', models.BooleanField(default=False)),
                ('roadmap', models.BooleanField(default=False)),
                ('license', models.CharField(default='MIT', max_length=20)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RoadMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='badge',
            options={},
        ),
        migrations.AlterModelOptions(
            name='command',
            options={},
        ),
        migrations.AlterModelOptions(
            name='tool',
            options={},
        ),
        migrations.CreateModel(
            name='ProjectTool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.project')),
                ('tool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tool')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectRoadMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('done', models.BooleanField(default=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.project')),
                ('road_map', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.roadmap')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectCommand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('step', models.IntegerField(default=1)),
                ('command', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.command')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.project')),
                ('tool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tool')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectBadge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('badge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.badge')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.project')),
            ],
        ),
    ]