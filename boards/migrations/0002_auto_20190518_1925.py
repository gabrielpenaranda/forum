# Generated by Django 2.2 on 2019-05-18 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='board',
            options={'ordering': ['name'], 'verbose_name': 'Tablero', 'verbose_name_plural': 'Tableros'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_at'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['subject'], 'verbose_name': 'Tópico', 'verbose_name_plural': 'Tópicos'},
        ),
    ]