# Generated by Django 5.1.4 on 2025-01-06 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_contact_alter_awarts_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='agress',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='photo',
            new_name='phone',
        ),
        migrations.AddField(
            model_name='contact',
            name='description_2',
            field=models.TextField(default=1, verbose_name='Описание нижнего загаловка'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='title_2',
            field=models.CharField(default=1, max_length=255, verbose_name='Нижний загаловок'),
            preserve_default=False,
        ),
    ]
