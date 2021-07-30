# Generated by Django 3.2.5 on 2021-07-29 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_prueba_curso'),
    ]

    operations = [
        migrations.CreateModel(
            name='curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.CharField(blank=True, max_length=200, null=True, verbose_name='Curso')),
                ('tipo_curso', models.CharField(blank=True, max_length=300, null=True, verbose_name='Tipo de Curso')),
                ('desc_curso', models.CharField(blank=True, max_length=300, null=True, verbose_name='Tipo de Curso')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
                'ordering': ['id'],
            },
        ),
        migrations.RemoveField(
            model_name='prueba',
            name='curso',
        ),
        migrations.AlterField(
            model_name='prueba',
            name='tipo_prueba',
            field=models.CharField(max_length=50, verbose_name='tipo_prueba'),
        ),
    ]
