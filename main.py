from sys import argv
from processing import load_ini, load_csv, load_stat, fit, process

def main():
    print('description')

    print('*****')

    if len(argv) != 2:
        print('*****program aborted*****')
        return None

    try:
        print(f'ini {argv[1]}: ', end='')
        input, output = load_ini(argv[1])
    except Exception:
        print('\n*****program aborted*****')
        return None
    else:
        print('OK')

    try:
        print(f'input-csv {input["csv"]}: ', end='')
        csv = load_csv(input)
    except Exception:
        print('\n*****program aborted*****')
        return None
    else:
        print('OK')

    try:
        print(f'input-json {input["json"]}: ', end='')
        json = load_stat(input)
    except Exception:
        print('\n*****program aborted*****')
        return None
    else:
        print('OK')

    print('json?=csv: ', end='')
    if fit(csv, json):
        print('OK')
    else:
        print('UPS')

if __name__ == '__main__':
    main()
