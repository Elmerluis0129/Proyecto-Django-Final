# Generated by Django 5.1.3 on 2024-12-03 00:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiApp', '0010_alter_tutoria_estudiantes_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudtutoria',
            name='estado',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('Aprobado', 'Aprobado')], max_length=50),
        ),
        migrations.AlterField(
            model_name='solicitudtutoria',
            name='estudiante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes_tutorias', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='solicitudtutoria',
            name='nombre_tutoria',
            field=models.CharField(max_length=100),
        ),
    ]
