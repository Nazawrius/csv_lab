from sys import argv

def load_data(ini_path):
    with open(ini_path, 'r') as ini:
        for line in ini:
            print(line, end='')

def main():
    print('description')
    print('*****')
    load_data(argv[1])

if __name__ == '__main__':
    main()
