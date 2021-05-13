class Invoice:
    def __init__(self, row):
        if len(row) != 6:
            raise Exception

        if len(row[0]) == 11 and row[0].isalnum() and row[0].strip() == row[0]:
            self.id = row[0]
        else:
            raise Exception

        self.entries = dict()
        self.number_of_repeats = dict()
        self.total_entries = 0
        self.total_number = 0
        self.total_cost = 0
        self.add_entry(row[1:])

    def add_entry(self, row):
        number = row[0]
        if number.isdigit() and number[0] != 0:
            self.entries[int(number)] = Entry(row[1:])
        else:
            raise Exception

        entry = self.entries[int(number)]
        if entry.name in self.number_of_repeats:
            self.number_of_repeats[entry.name] += 1
        else:
            self.number_of_repeats[entry.name] = 1

        self.total_entries += 1
        self.total_number += entry.number
        self.total_cost += entry.cost

    def __repr__(self):
        s = f'{self.id}\t{self.total_number}\t{self.total_entries}\t{self.total_cost}\n'
        for key in sorted(self.entries.keys()):
            s += f'\t{key}\t{self.entries[key]}\t{key}\n'
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
