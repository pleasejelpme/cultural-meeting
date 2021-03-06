# Generated by Django 3.2 on 2022-05-22 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='email')),
                ('fecha_creado', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='')),
                ('ciudad_origen', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='meetings.ciudad')),
                ('intereses', models.ManyToManyField(to='meetings.Categoria')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
