# Generated by Django 3.2.5 on 2021-07-21 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210721_2245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fecha',
            name='id_prueba',
        ),
    ]