# Generated by Django 3.2.5 on 2021-07-29 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20210729_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prueba',
            name='id_curso',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.curso'),
        ),
    ]
