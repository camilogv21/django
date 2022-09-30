# Generated by Django 4.0.6 on 2022-09-02 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('territorium', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254)),
                ('usuario', models.CharField(max_length=100)),
                ('clave', models.CharField(max_length=254)),
                ('rol', models.CharField(choices=[('R', 'administrador'), ('I', 'instructor'), ('A', 'aprendiz')], default='A', max_length=1)),
            ],
        ),
    ]
