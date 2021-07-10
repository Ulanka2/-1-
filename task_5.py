import csv
import string, pandas
from faker import Faker
from faker.providers import internet
fake = Faker(['ru_RU'])
fake.add_provider(internet)

class Generation_Name:
    USERS = []
    IP_ADRES = []
    def __init__(self):
        self.fake = Faker(['ru_RU'])

    def get_100_name(self):
        for i in range(100):
            USERS = self.fake.name()
            self.USERS.append(USERS)
            IP_ADRES = self.fake.ipv4_private()
            self.IP_ADRES.append(IP_ADRES)

class Writer:
    def __init__(self, parser):
        self.parser = parser
        self.csv_write = pandas.DataFrame({'USERS':parser.USERS,'IP_ADRES':parser.IP_ADRES})# 1. Сортировка по 1 полю
    
    def write_to_csv(self):
        with open('name.csv', 'w') as file:
            file.write(self.csv_write.to_csv(index=False))
            file_writer = csv.writer(file, delimiter = ",", lineterminator="\r")# 2. Добавление строки
            file_writer.writerow(["Азимов улан Шарабидинович", "199.28.214.152"])



p = Generation_Name()
p.get_100_name()
w = Writer(p)
w.write_to_csv()

# 3. Обновление строки
# 4. Редактирование строки
# 5. Поиск элементов по заданному условию
