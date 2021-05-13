class Invoice:
    def __init__(self, row):
        self.number = row[0]
        if not(len(self.number) == 11 and self.number.isalnum()):
            raise Exception

        self.entries = dict()
        self.add_product(row[1:])

    def add_product(self, row):
        number = row[0]
        if not number.isdigit() or number[0] == 0:
            raise Exception
        else:
            self.entries[int(number)] = Entry(row[2:])

    def __repr__(self): #Not finished!!!
        s = self.number + '\n'
        for key in sorted(self.entries.keys()):
            s += '\t' + str(key) + '\t' + str(self.entries[key]) + '\n'
        return s


class Entry:
    def __init__(self, row):
        ...

    def __repr__(self):
        return ''
