from django.db import models


class train_inf(models.Model):
    number = models.CharField('Номер', max_length=10)
    link = models.CharField('Ссылка', max_length=350)
    city_iz = models.CharField('Город отправления', max_length=20)
    vokzal_iz = models.CharField('Вокзал отправления', max_length=20)
    time_iz = models.CharField('Время отправления', max_length=10)
    date_iz = models.DateField('Дата отправления')
    city_v = models.CharField('Город прибытия', max_length=20)
    vokzal_v = models.CharField('Вокзал прибытия', max_length=20)
    time_v = models.CharField('Время прибытия', max_length=10)
    date_v = models.DateField('Дата прибытия')
    price_1 = models.FloatField('Плацкарт')
    price_2 = models.FloatField('Купе')
    price_3 = models.FloatField('СВ')
    price_4 = models.FloatField('Цена4', default=0)
    price_5 = models.FloatField('Цена5', default=0)

    def __str__(self):
        return self.number + ' : ' + self.city_iz + ' --- ' + self.city_v


class train_sr(models.Model):
    city_iz = models.CharField('Город отправления', max_length=20)
    date_iz = models.DateField('Дата отправления')
    city_v = models.CharField('Город прибытия', max_length=20)
    date_v = models.DateField('Дата прибытия')
    price_1 = models.FloatField('Плацкарт')
    price_2 = models.FloatField('Купе')
    price_3 = models.FloatField('СВ')
    price_4 = models.FloatField('Цена4', default=0)
    price_5 = models.FloatField('Цена5', default=0)

    def __str__(self):
        return self.city_iz + ' --- ' + self.city_v


class hotel_info(models.Model):
    city = models.CharField('Город', max_length=20)
    date_start = models.DateField('Дата начала')
    date_finish = models.DateField('Дата окончания')
    price = models.FloatField('Средняя цена')

    def __str__(self):
        return self.city + ': ' + str(self.date_start) + '--' + str(self.date_finish)


class avia_info(models.Model):
    city_iz = models.CharField('Город отправления', max_length=20)
    city_v = models.CharField('Город прибытия', max_length=20)
    date_start = models.DateField('Дата начала')
    date_finish = models.DateField('Дата окончания')
    price = models.FloatField('Средняя цена')

    def __str__(self):
        return self.city_iz + '---' + self.city_v
