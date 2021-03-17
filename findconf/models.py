from django.db import models

class train_info(models.Model):
    number = models.IntegerField('Номер')
    link = models.CharField('Ссылка', max_length=300)
    city_iz = models.CharField('Город отправления', max_length=20)
    vokzal_iz = models.CharField('Вокзал отправления', max_length=20)
    city_v = models.CharField('Город прибытия', max_length=20)
    vokzal_v = models.CharField('Вокзал прибытия', max_length=20)
    time_iz = models.TimeField('Время отправления')
    date_iz = models.DateField('Дата отправления')
    date_v = models.DateField('Дата прибытия')
    category1 = models.CharField('Категория1', max_length=20)
    price_1 = models.FloatField('Цена1')
    category2 = models.CharField('Категория2', max_length=20)
    price_2 = models.FloatField('Цена2')
    category3 = models.CharField('Категория3', max_length=20)
    price_3 = models.FloatField('Цена3')

    def __str__(self):
        return self.link