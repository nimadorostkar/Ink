# Generated by Django 5.0.2 on 2024-03-07 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='design',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
