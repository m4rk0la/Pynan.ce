# Generated by Django 4.2.3 on 2023-07-04 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conta',
            name='banco',
            field=models.CharField(choices=[('NU', 'Nubank'), ('CE', 'Caixa econômica'), ('BD', 'Bradesco'), ('IN', 'Inter'), ('BB', 'Banco do Brasil'), ('BR', 'BRB')], max_length=2),
        ),
    ]
