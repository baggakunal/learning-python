import sys


def print_file(file_path):
    try:
        file = None
        file = open(file_path, mode='rt', encoding='utf-8')
        for line in file:
            sys.stdout.write(line)

    except FileNotFoundError:
        print('File path is invalid')

    finally:
        if file:
            file.close()


if __name__ == '__main__':
    print_file(sys.argv[1])
