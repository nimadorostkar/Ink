# Generated by Django 5.0.2 on 2024-03-08 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_alter_homepageinfo_about_me'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepageinfo',
            old_name='my_transparent_img',
            new_name='my_img',
        ),
    ]
