# Generated by Django 5.0.2 on 2024-03-17 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_pessoa_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicoespecialidade',
            name='especialidade',
        ),
        migrations.RemoveField(
            model_name='medicoespecialidade',
            name='medico',
        ),
        migrations.RemoveField(
            model_name='medico',
            name='especialidade',
        ),
        migrations.DeleteModel(
            name='Endereco',
        ),
        migrations.DeleteModel(
            name='Especialidade',
        ),
        migrations.DeleteModel(
            name='MedicoEspecialidade',
        ),
    ]
