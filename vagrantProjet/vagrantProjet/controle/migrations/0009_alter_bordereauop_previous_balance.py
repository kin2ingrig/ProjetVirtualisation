# Generated by Django 4.2.6 on 2023-12-21 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0008_alter_bordereauop_transfer_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bordereauop',
            name='PREVIOUS_BALANCE',
            field=models.IntegerField(null=True),
        ),
    ]
