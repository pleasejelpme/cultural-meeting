# Generated by Django 3.2 on 2022-05-22 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ciudad',
            options={'verbose_name_plural': 'Ciudades'},
        ),
        migrations.AddField(
            model_name='meeting',
            name='direccion',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]