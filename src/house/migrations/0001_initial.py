# Generated by Django 2.2.19 on 2021-02-28 09:58

from django.db import migrations, models
import django.db.models.deletion
import house.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('image', models.FileField(blank=True, null=True, upload_to=house.models.GenerateHouseImagePath())),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('points', models.IntegerField(default=0)),
                ('completed_tasks_count', models.IntegerField(default=0)),
                ('not_completed_tasks_count', models.IntegerField(default=0)),
                ('manager', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='managed_house', to='users.Profile')),
            ],
        ),
    ]
