# Generated by Django 4.1.3 on 2023-06-19 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passwordgenerator', '0003_alter_passgenerator_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passgenerator',
            name='lettercase',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='passgenerator',
            name='lowercase',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='passgenerator',
            name='number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='passgenerator',
            name='symbols',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
