# Generated by Django 4.2.5 on 2023-12-22 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_questao_topico_resposta_questao_topico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='tipo_usuario',
            field=models.CharField(choices=[('ALUNO', 'Aluno'), ('PROFESSOR', 'Professor'), ('ADMIN', 'Admin')], max_length=10),
        ),
    ]
