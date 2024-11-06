# Generated by Django 5.1 on 2024-11-06 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('Codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=100)),
                ('Creditos', models.PositiveBigIntegerField()),
            ],
        ),
    ]