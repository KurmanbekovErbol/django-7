# Generated by Django 5.1.4 on 2025-01-06 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_over'),
    ]

    operations = [
        migrations.CreateModel(
            name='Awarts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='awarts/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'О нас (галерея)',
            },
        ),
    ]
