# Generated by Django 3.2.5 on 2021-07-29 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_alter_prueba_id_curso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prueba',
            name='id_curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.curso'),
        ),
    ]
