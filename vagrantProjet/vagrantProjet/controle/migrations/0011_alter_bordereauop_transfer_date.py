# Generated by Django 4.2.6 on 2023-12-21 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0010_alter_bordereauop_previous_balance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bordereauop',
            name='TRANSFER_DATE',
            field=models.DateField(default=''),
        ),
    ]
