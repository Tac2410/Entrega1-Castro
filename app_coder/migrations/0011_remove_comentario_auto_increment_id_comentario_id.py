# Generated by Django 4.0.3 on 2022-04-28 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_coder', '0010_comentario_auto_increment_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='auto_increment_id',
        ),
        migrations.AddField(
            model_name='comentario',
            name='id',
            field=models.BigAutoField(auto_created=True, default=2, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]