# Generated by Django 3.1.4 on 2020-12-17 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfissionalSaude',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funcao', models.CharField(max_length=255)),
                ('pessoas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pessoa', to='administracao.pessoa')),
            ],
        ),
    ]
