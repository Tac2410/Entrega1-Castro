# Generated by Django 4.0.3 on 2022-04-28 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensajes', '0002_alter_mensajes_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mensajes',
            old_name='id',
            new_name='ida',
        ),
    ]
