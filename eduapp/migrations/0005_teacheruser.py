# Generated by Django 4.1.7 on 2023-04-12 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eduapp', '0004_rename_courses_addstud_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='teacheruser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('number', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, default='default1.jpg', null=True, upload_to='image/')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eduapp.course')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]