class Invoice:
    """
    Class for handling invoices
    """
    def __init__(self, row):
        if len(row) != 6:
            raise Exception("Invoice validation error")

        id = row[0]
        if len(id) == 11 and id.isalnum() and id.strip() == id:
            self._id = row[0]
        else:
            raise Exception("Invoice name validation error")

        self._entries = dict()
        self._number_of_repeats = dict()
        self._total_entries = 0
        self._total_number = 0
        self._total_cost = 0
        self.add_entry(row[1:])

    @property
    def total_number(self):
        return self._total_number

    @property
    def total_entries(self):
        return self._total_entries

    @property
    def entries(self):
        return self._entries

    @property
    def number_of_repeats(self):
        return self._number_of_repeats

    def add_entry(self, row):
        """
        add_entry(self, row, /)

        Adds an entry to invoice
        """
        number = row[0]
        if number.isdigit() and number[0] != 0:
            self._entries[int(number)] = Entry(row[1:])
        else:
            raise Exception("Entry number validation error")

        entry = self._entries[int(number)]
        if entry.name in self._number_of_repeats:
            self._number_of_repeats[entry.name] += 1
        else:
            self._number_of_repeats[entry.name] = 1

        self._total_entries += 1
        self._total_number += entry.number
        self._total_cost += entry.cost

    def __repr__(self):
        return f'{self._id}\t{self._total_number:.3f}\t{self._total_entries}\t{self._total_cost:.2f}\n'


class Entry:
    """
    Class for handling entries
    """
    def __init__(self, row):
        name_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '-_"
        name = row[0]
        if all((ch in name_chars for ch in name)) and 2 <= len(name) <= 26 and name.strip() == name:
            self._name = name
        else:
            raise Exception("Entry name validation error")

        price = row[1]
        if price[-3] == '.' and float(price) > 0:
            self._price = float(price)
        else:
            raise Exception("Entry price validation error")

        number = row[2]
        if number[-4] == '.' and float(number) > 0:
            self._number = float(number)
        else:
            raise Exception("Entry number validation error")

        wanted_cost = self._price * self._number
        cost = row[3]
        if cost[-3] == '.' and cost == f'{wanted_cost:.2f}':
            self._cost = float(cost)
        else:
            raise Exception("Entry cost validation error")

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def number(self):
        return self._number

    @property
    def cost(self):
        return self._cost

    def __repr__(self):
        return f'{self._name}\t{self._price:.2f}\t{self._number:.3f}\t{self._cost:.2f}'
