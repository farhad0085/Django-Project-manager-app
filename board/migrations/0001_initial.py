# Generated by Django 4.2.13 on 2024-07-14 20:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100, verbose_name='Project title')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Short description')),
                ('working', models.BooleanField(default=True, verbose_name='Currently working')),
                ('color', models.CharField(choices=[('default', 'Default'), ('black', 'Black'), ('green', 'Green'), ('orange', 'Orange'), ('blue', 'Blue'), ('violet', 'Violet'), ('red', 'Red'), ('yellow', 'Yellow')], default='default', max_length=15, verbose_name='Project UI color')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100, verbose_name='Card title')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Short description')),
                ('color', models.CharField(choices=[('default', 'Default'), ('black', 'Black'), ('green', 'Green'), ('orange', 'Orange'), ('blue', 'Blue'), ('violet', 'Violet'), ('red', 'Red'), ('yellow', 'Yellow')], default='default', max_length=15, verbose_name='Card color')),
                ('board', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='board.board')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Card',
                'verbose_name_plural': 'Cards',
            },
        ),
        migrations.CreateModel(
            name='CardItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100, verbose_name='Item title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Short description')),
                ('working', models.BooleanField(default=True, verbose_name='Currently working')),
                ('card', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='board.card')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
            ],
            options={
                'verbose_name': 'Card Item',
                'verbose_name_plural': 'Card Items',
            },
        ),
        migrations.CreateModel(
            name='CardItemComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('body', models.TextField(verbose_name='Comment text')),
                ('card_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='board.carditem')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Card Item Comment',
                'verbose_name_plural': 'Card Item Comments',
            },
        ),
    ]