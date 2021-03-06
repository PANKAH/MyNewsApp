# Generated by Django 2.2.5 on 2020-05-03 00:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import news.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('date_published', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('Published', 'published'), ('Drafted', 'drafted')], default='Drafted', max_length=200)),
                ('tag', models.CharField(blank=True, max_length=100, null=True, verbose_name=news.models.Category)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('date_published',),
            },
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('fav_tag', models.CharField(max_length=100, verbose_name=news.models.Category)),
                ('history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='news.Post')),
                ('starred', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='starred', to='news.Post')),
            ],
        ),
    ]
