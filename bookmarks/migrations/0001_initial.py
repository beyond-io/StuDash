# Generated by Django 3.1.4 on 2020-12-19 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('grades', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('urlname', models.CharField(max_length=30)),
                ('last_view_date', models.DateTimeField(auto_now=True, null=True)),
                ('course', models.ForeignKey(default='SOME STRING',
                    on_delete=django.db.models.deletion.CASCADE, to='grades.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
