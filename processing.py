import json, csv
from models import Invoice, Entry


def load_ini(ini_path):
    """
    load_ini(ini_path, /)

    Reading settings from .ini
    """
    ini = json.load(open(ini_path, 'r'))

    if 'input' not in ini or 'output' not in ini:
        raise Exception(".ini fields validation error")

    input = ini['input']
    if 'json' not in input or 'csv' not in input or 'encoding' not in input:
        raise Exception("input fields validation error")

    output = ini['output']
    if 'fname' not in output or 'encoding' not in output:
        raise Exception("output fields validation error")

    return input, output


def load_csv(input):
    """
    load_csv(input, /)

    Reading data from .csv
    """
    with open(input['csv'], 'r', encoding=input['encoding']) as f:
        invoice_dict = dict()
        reader = csv.reader(f, delimiter=';')

        for row in reader:
            invoice_id = row[0]

            if invoice_id in invoice_dict:
                invoice_dict[invoice_id].add_entry(row[1:])
            else:
                invoice_dict[invoice_id] = Invoice(row)

        return invoice_dict


def load_stat(input):
    """
    load_stat(input, /)

    Reading options from .json
    """
    with open(input['json'], 'r', encoding=input['encoding']) as f:
        return dict(json.load(f))


def fit(stat, invoices):
    """
    fit(stat, invoices, /)

    Checking if .csv data fits .json options
    """
    total_entries = sum(invoice.total_entries for invoice in invoices.values())
    total_number = sum(invoice.total_number for invoice in invoices.values())

    return stat["загальна кількість записів"] == total_entries and stat["сума кількостей"] == total_number


def key_func(entry):
    """
    key_func(entry, /)

    Key function for sorting invoice entries
    """
    return (entry[1].name, entry[1].number, entry[1].price)

def process(invoices, output):
    """
    process(invoices, output, /)

    Processing .csv data and outputing into .txt
    """
    with open(output["fname"], 'w', encoding=output["encoding"]) as f:
        for invoice in invoices.values():
            flag = False
            repeating_entries = set()

            for key, entry in invoice.entries.items():
                if invoice.number_of_repeats[entry.name] > 1:
                    flag = True
                    repeating_entries.add((key, invoice.entries[key]))

            if flag:
                f.write(str(invoice))
                for key, entry in sorted(repeating_entries, key=key_func):
                    f.write(f'\t{str(entry)} {str(key)}\n')
