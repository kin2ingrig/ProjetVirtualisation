# Generated by Django 4.2.6 on 2023-12-21 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0005_bordereauop_agence_bordereauop_operateur_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bordereauop',
            old_name='amount',
            new_name='POST_BALANCE',
        ),
        migrations.RenameField(
            model_name='bordereauop',
            old_name='previous',
            new_name='PREVIOUS_BALANCE',
        ),
        migrations.RenameField(
            model_name='bordereauop',
            old_name='number',
            new_name='REFERENCE_NUMBER',
        ),
        migrations.RenameField(
            model_name='bordereauop',
            old_name='statement',
            new_name='STATEMENT',
        ),
        migrations.RenameField(
            model_name='bordereauop',
            old_name='post',
            new_name='TRANSFER_AMOUNT',
        ),
        migrations.RenameField(
            model_name='bordereauop',
            old_name='date',
            new_name='TRANSFER_DATE',
        ),
        migrations.RenameField(
            model_name='bordereauop',
            old_name='idtransfer',
            new_name='TRANSFER_ID',
        ),
    ]
