# Generated by Django 2.2.19 on 2021-02-28 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_profile_house'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('NC', 'Not Completed'), ('C', 'Completed')], default='NC', max_length=2)),
                ('completed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='completed_tasks', to='users.Profile')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_tasks', to='users.Profile')),
            ],
        ),
    ]
