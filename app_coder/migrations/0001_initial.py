# Generated by Django 4.0.3 on 2022-03-30 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('nombre', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Commentario',
            fields=[
                ('titulo', models.CharField(max_length=100)),
                ('mensaje', models.CharField(max_length=1000)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('auto_increment_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Ususario',
            fields=[
                ('nombre', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]