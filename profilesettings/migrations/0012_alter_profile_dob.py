# Generated by Django 4.2.7 on 2024-01-11 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profilesettings', '0011_rename_username_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
