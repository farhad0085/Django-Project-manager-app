# Generated by Django 4.2.13 on 2024-06-10 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='color',
            field=models.CharField(choices=[('default', 'Default'), ('black', 'Black'), ('green', 'Green'), ('orange', 'Orange'), ('blue', 'Blue'), ('violet', 'Violet'), ('red', 'Red'), ('yellow', 'Yellow')], default='default', max_length=15, verbose_name='Card color'),
        ),
    ]
