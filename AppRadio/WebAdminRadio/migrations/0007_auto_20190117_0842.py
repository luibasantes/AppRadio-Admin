# Generated by Django 2.1.1 on 2019-01-17 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebAdminRadio', '0006_auto_20190117_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenes',
            name='url',
            field=models.CharField(editable=False, max_length=150),
        ),
    ]