import string, pandas
from faker import Faker

class Generation_Name:
    NAME = []
    def __init__(self):
        self.fake = Faker(['ru_RU'])

    def get_100_name(self):
        for i in range(100):
            NAME = self.fake.name()
            self.NAME.append(NAME)

class Writer:
    def __init__(self, parser):
        self.parser = parser
        self.csv_write = pandas.DataFrame({'FIRST NAME LAST NAME MIDDLE NAME ':parser.NAME})
    
    def write_to_csv(self):
        with open('name.csv', 'w') as file:
            file.write(self.csv_write.to_csv(index=False))



p = Generation_Name()
p.get_100_name()
w = Writer(p)
w.write_to_csv()