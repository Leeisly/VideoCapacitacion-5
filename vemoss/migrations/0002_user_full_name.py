# Generated by Django 2.1.15 on 2021-04-07 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vemoss', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
