# Generated by Django 4.1.3 on 2023-06-17 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passwordgenerator', '0002_passgenerator_symbols_alter_passgenerator_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passgenerator',
            name='number',
            field=models.IntegerField(max_length=15),
        ),
    ]