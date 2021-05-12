from sys import argv
import json

def load_data(ini_path):
    ini = json.load(open(ini_path))

    if 'input' not in ini or 'output' not in 'ini':
        raise Exception

    input = ini['input']
    if 'json' not in input or 'csv' not in input or 'encoding' not in input:
        raise Exception

    output = ini['output']
    if 'fname' not in output or 'encoding' not in output:
        raise Exception

    return input, output

def main():
    print('description')

    print('*****')

    if len(argv) != 2:
        print('*****program aborted*****')
        return None

    try:
        input, output = load_data(argv[1])
    except Exception:
        print('*****program aborted*****')
        return None
    else:
        print(f'ini {argv[1]}: OK')

if __name__ == '__main__':
    main()
