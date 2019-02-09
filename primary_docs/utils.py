import os

import requests
import re
from openpyxl import load_workbook

from .models import Worker, Station, Position, Car, CHOICES_OF_KIND


class Synchronizer:
    # Синхронизатор базы данных с внешним 1С-сервером

    API = 'http://192.168.0.38:81/hrm/hs/{0}/{1}/'

    STATIONS = {
    'Фомин': Station.objects.get(name="Фоминский производственный участок"),
    'Волошин': Station.objects.get(name="Волошинский производственный участок"),
    'Калитвен': Station.objects.get(name="Калитвенский производственный участок"),
    'Большин': Station.objects.get(name="Большинский производственный участок"),
    'Криворож': Station.objects.get(name="Криворожский производственный участок"),
    'Милллер': Station.objects.get(name="Миллеровский производственный участок"),
    'Городищ': Station.objects.get(name="Городищенский производственный участок"),
    'Митякин': Station.objects.get(name="Митякинский производственный участок")
    }

    # Получение данных из 1С сервера
    def _getData(self, resource):
        try:
            response = requests.get(self.API.format('getdata', resource))
        except Exception as e:
            print('1С-сервер не доступен!')
        else:
            if response.ok:
                try:
                    data = response.json()
                except Exception as e:
                    print('Ошибка формата данных')
                else:
                    return data
                finally:
                    response.close()
            else:
                print('Ошибка при подключении к 1С-серверу, код: {}'.format(response.status_code))

    # Парсинг XLS-файла, и выгрузка автомобилей из онного
    def load_cars_from_xls(path):
        if os.path.exists(path):
            try:
                wb = load_workbook(path)
            except Exception as e:
                print('Неверный формат файла')
            else:
                sheet = wb.active
                counter = 0
                kinds = dict(reversed(x) for x in CHOICES_OF_KIND)
                for row in sheet.rows:
                    new_car = dict(
                            kind=kinds[row[0].value],
                            name=row[1].value,
                            number=row[2].value,
                            station=Station.objects.get(pk=row[3].value),
                        )
                    instance, created = Car.objects.get_or_create(**new_car)
                    if created:
                        counter += 1
                print(
                    'Созданно {0} новых единиц техники, всего в системе {1} едениц техники'.format(
                            counter, Car.objects.count()
                        )
                    )
        else:
            print('Файл {} не найден'.format(path))

    def get_workers(self):
        data = self._getData('workers')
        if data and data.get('workers'):
            counter = 0
            workers = data.get('workers')
            for worker in workers:
                position, created = Position.objects.get_or_create(name=worker['position']['name'])
                new_worker = dict(
                        name=worker['name'],
                        surname=worker['surname'],
                        patronymic=worker['patronymic'],
                        rank="1",
                        position=position
                    )
                for st in self.STATIONS.keys():
                    pattern = re.template(st)
                    if pattern.search(worker['station']['name']):
                        new_worker['station'] = self.STATIONS[st]
                instance, created = Worker.objects.get_or_create(**new_worker)
                if created:
                    counter += 1
            print(
                'Созданно {0} новых работников, всего в системе {1} работников'.format(
                    counter, Worker.objects.count()
                    )
                )


