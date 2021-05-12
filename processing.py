import json, csv

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
        return list(csv.reader(f, delimiter=';'))

def load_stat(input):
    return dict(json.load(open(input['json'], 'r', encoding=input['encoding'])))

def fit(j, c):
    ...

def process():
    ...
