from sys import argv
from processing import load_ini, load_csv, load_stat, fit, process
from debug import abort

def main():
    """
    main(/)

    Main function
    """
    print('description')

    print('*****')

    if len(argv) != 2:
        abort('Missing/unnecessary command line arguments')
        return None

    print(f'ini {argv[1]}: ', end='')
    try:
        input, output = load_ini(argv[1])
    except Exception as e:
        abort(e)
        return None
    else:
        print('OK')

    print(f'input-csv {input["csv"]}: ', end='')
    try:
        invoices = load_csv(input)
    except Exception as e:
        abort(e)
        return None
    else:
        print('OK')

    print(f'input-json {input["json"]}: ', end='')
    try:
        stat = load_stat(input)
    except Exception as e:
        abort(e)
        return None
    else:
        print('OK')

    print('json?=csv: ', end='')
    if fit(stat, invoices):
        print('OK')
    else:
        print('UPS')

    print(f'output {output["fname"]}: ', end='')
    try:
        process(invoices, output)
    except Exception as e:
        abort(e)
        return None
    else:
        print('OK')

if __name__ == '__main__':
    main()
