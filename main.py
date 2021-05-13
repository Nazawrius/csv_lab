from sys import argv
from processing import load_ini, load_csv, load_stat, fit, process

def main():
    print('description')

    print('*****')

    if len(argv) != 2:
        print('*****program aborted*****')
        return None

    print(f'ini {argv[1]}: ', end='')
    try:
        input, output = load_ini(argv[1])
    except Exception:
        print('\n*****program aborted*****')
        return None
    else:
        print('OK')

    print(f'input-csv {input["csv"]}: ', end='')
    try:
        data = load_csv(input)
    except Exception:
        print('\n*****program aborted*****')
        return None
    else:
        print('OK')

    print(f'input-json {input["json"]}: ', end='')
    try:
        stat = load_stat(input)
    except Exception:
        print('\n*****program aborted*****')
        return None
    else:
        print('OK')

    print('json?=csv: ', end='')
    if fit(stat, data):
        print('OK')
    else:
        print('UPS')

    print(f'output {output["fname"]}: ', end='')
    try:
        process(data, output)
    except Exception:
        print('\n*****program aborted*****')
        return None
    else:
        print('OK')

if __name__ == '__main__':
    main()
