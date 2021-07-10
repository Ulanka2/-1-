import string, random, pandas

# def random_phone(len):
#     return ''.join(random.choice(string.digits) for i in range(len))

# code = ['+996777', '+996555', '+996700']

# for i in range(1000):
#     print((random.choice(code) + random_phone(6)))


class Phone:
    BEELINE = []
    MEGACOM = []
    O = []
    def __init__(self):
        self.code = ['+996777', '+996555', '+996700']

    def phone(self,len):
        get_num = ''.join(random.choice(string.digits) for i in range(len))
        return  get_num

    def get_1000_phone(self):
        for i in range(100):
            BEELINE = self.code[0] + self.phone(6)
            print(self.BEELINE.append(BEELINE))
            MEGACOM = self.code[1] + self.phone(6)
            self.MEGACOM.append(MEGACOM)
            O = self.code[2] + self.phone(6)
            self.O.append(O)
            
      

class Writer:
    def __init__(self, parser):
        self.parser = parser
        self.csv_write = pandas.DataFrame({'\t''BEELINE':parser.BEELINE,'\t''MEGACOM!':parser.MEGACOM,'\t\t''O!':parser.O})
        # self.csv_write = self.csv_write.transpose()
    
    def write_to_csv(self):
        with open('phone.csv', 'w') as file:
            file.write(self.csv_write.to_csv(index=False))

p = Phone()
p.get_1000_phone()
w = Writer(p)
w.write_to_csv()