# Generated by Django 2.1.1 on 2018-10-03 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebAdminRadio', '0004_remove_emisora_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='segmento',
            name='slug',
        ),
    ]
