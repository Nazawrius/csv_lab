import json, csv
from models import Invoice, Entry


def load_ini(ini_path):
    ini = json.load(open(ini_path, 'r'))

    if 'input' not in ini or 'output' not in ini:
        raise Exception

    input = ini['input']
    if 'json' not in input or 'csv' not in input or 'encoding' not in input:
        raise Exception

    output = ini['output']
    if 'fname' not in output or 'encoding' not in output:
        raise Exception

    return input, output


def load_csv(input):
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
    with open(input['json'], 'r', encoding=input['encoding']) as f:
        return dict(json.load(f))


def fit(stat, invoices):
    total_entries = sum(invoice.total_entries for invoice in invoices.values())
    total_number = sum(invoice.total_number for invoice in invoices.values())

    return stat["загальна кількість записів"] == total_entries and stat["сума кількостей"] == total_number


def process(invoices, output):
    with open(output["fname"], 'w', encoding=output["encoding"]) as f:
        for id, invoice in invoices.items():
            f.write(str(invoice))
