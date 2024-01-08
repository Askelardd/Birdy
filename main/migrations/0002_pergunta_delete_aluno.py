# Generated by Django 4.2.5 on 2023-12-11 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta_texto', models.CharField(max_length=200)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='assets/')),
                ('resposta1', models.CharField(max_length=200)),
                ('resposta2', models.CharField(max_length=200)),
                ('resposta3', models.CharField(max_length=200)),
                ('resposta4', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='aluno',
        ),
    ]