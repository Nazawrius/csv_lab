class Invoice:
    """
    Class for handling invoices
    """
    def __init__(self, row):
        if len(row) != 6:
            raise Exception("Invoice validation error")

        if len(row[0]) == 11 and row[0].isalnum() and row[0].strip() == row[0]:
            self.id = row[0]
        else:
            raise Exception("Invoice name validation error")

        self.entries = dict()
        self.number_of_repeats = dict()
        self.total_entries = 0
        self.total_number = 0
        self.total_cost = 0
        self.add_entry(row[1:])

    def add_entry(self, row):
        """
        add_entry(self, row, /)
        
        Adds an entry to invoice
        """
        number = row[0]
        if number.isdigit() and number[0] != 0:
            self.entries[int(number)] = Entry(row[1:])
        else:
            raise Exception("Entry validation error")

        entry = self.entries[int(number)]
        if entry.name in self.number_of_repeats:
            self.number_of_repeats[entry.name] += 1
        else:
            self.number_of_repeats[entry.name] = 1

        self.total_entries += 1
        self.total_number += entry.number
        self.total_cost += entry.cost

    def __repr__(self):
        return f'{self.id} {self.total_number:.3f} {self.total_entries} {self.total_cost:.2f}\n'


class Entry:
    """
    Class for handling entries
    """
    def __init__(self, row):
        name_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '-_"
        if all((ch in name_chars for ch in row[0])) and 2 <= len(row[0]) <= 26 and row[0].strip() == row[0]:
            self.name = row[0]
        else:
            raise Exception("Entry name validation error")

        if row[1][-3] == '.' and float(row[1]) > 0:
            self.price = float(row[1])
        else:
            raise Exception("Entry price validation error")

        if row[2][-4] == '.' and float(row[2]) > 0:
            self.number = float(row[2])
        else:
            raise Exception("Entry number validation error")

        cost = self.price * self.number
        if row[3][-3] == '.' and row[3] == f'{cost:.2f}':
            self.cost = float(row[3])
        else:
            raise Exception("Entry cost validation error")

    def __repr__(self):
        return f'{self.name} {self.price:.2f} {self.number:.3f} {self.cost:.2f}'
