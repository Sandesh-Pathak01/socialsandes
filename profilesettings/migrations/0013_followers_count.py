# Generated by Django 4.2.7 on 2024-01-17 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profilesettings', '0012_alter_profile_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='followers_count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.CharField(max_length=250)),
                ('user', models.CharField(max_length=250)),
            ],
        ),
    ]
