# Generated by Django 3.1.7 on 2021-03-21 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findconf', '0002_train_sr'),
    ]

    operations = [
        migrations.CreateModel(
            name='avia_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_iz', models.CharField(max_length=20, verbose_name='Город отправления')),
                ('city_v', models.CharField(max_length=20, verbose_name='Город прибытия')),
                ('date_start', models.DateField(verbose_name='Дата начала')),
                ('date_finish', models.DateField(verbose_name='Дата окончания')),
                ('price', models.FloatField(verbose_name='Средняя цена')),
            ],
        ),
        migrations.CreateModel(
            name='hotel_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20, verbose_name='Город')),
                ('date_start', models.DateField(verbose_name='Дата начала')),
                ('date_finish', models.DateField(verbose_name='Дата окончания')),
                ('price', models.FloatField(verbose_name='Средняя цена')),
            ],
        ),
    ]