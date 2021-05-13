class Invoice:
    def __init__(self, row):
        if len(row) != 6:
            raise Exception

        if len(row[0]) == 11 and row[0].isalnum() and row[0].strip() == row[0]:
            self.number = row[0]
        else:
            raise Exception

        self.entries = dict()
        self.number_of_repeats = dict()
        self.add_product(row[1:])

    def add_product(self, row):
        number = row[0]
        if number.isdigit() or number[0] != 0:
            self.entries[int(number)] = Entry(row[1:])
        else:
            raise Exception

        entry_name = self.entries[int(number)].name
        if entry_name in self.number_of_repeats:
            self.number_of_repeats[entry_name] += 1
        else:
            self.number_of_repeats[entry_name] = 1

    def __repr__(self): #Not finished!!!
        s = self.number + '\n'
        for key in sorted(self.entries.keys()):
            s += f'\t{key}\t{self.entries[key]}\n'
        return s


class Entry:
    def __init__(self, row):
        name_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '-_"
        if all((ch in name_chars for ch in row[0])) and 2 <= len(row[0]) <= 26 and row[0].strip() == row[0]:
            self.name = row[0]
        else:
            raise Exception

        if ... :
            self.price = float(row[1])

        if ... :
            self.number = float(row[2])

        if ... :
            self.cost = float(row[3])

    def __repr__(self):
        return f'{self.name}\t{self.price}\t{self.number}\t{self.cost}'
