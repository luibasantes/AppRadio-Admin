# Generated by Django 2.1.1 on 2018-10-03 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebAdminRadio', '0008_auto_20181003_0148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='activo',
        ),
    ]
