# Generated by Django 4.1.4 on 2023-04-27 12:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='events/')),
                ('event_type', models.CharField(choices=[('Online', 'Online'), ('Offline', 'Offline')], max_length=30)),
                ('description', models.TextField()),
                ('timezone', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_date', models.DateField()),
                ('end_time', models.TimeField()),
                ('link_to_event', models.CharField(blank=True, max_length=1000, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('is_published', models.BooleanField(default=True)),
                ('only_contacts', models.BooleanField(default=False)),
                ('is_publicly_available', models.BooleanField(default=True)),
                ('is_nobody', models.BooleanField(default=False)),
                ('schedule_post_date', models.DateField(blank=True, null=True)),
                ('schedule_post_time', models.TimeField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events_owner', to=settings.AUTH_USER_MODEL)),
                ('speakers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
