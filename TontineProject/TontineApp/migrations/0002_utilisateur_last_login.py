# Generated by Django 5.0.6 on 2025-02-02 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TontineApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
