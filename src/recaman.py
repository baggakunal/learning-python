import sys
from itertools import count, islice


def sequence():
    """Generate Recaman's sequence."""
    seen = set()
    a = 0
    for n in count(1):
        yield a
        seen.add(a)
        c = a - n
        if c < 0 or c in seen:
            c = a + n
        a = c


def write_sequence(filename, num):
    """Write Recaman's sequence to a text file."""
    try:
        file = open(filename, mode='wt', encoding='utf-8')
        file.writelines(f"{r}\n" for r in islice(sequence(), num + 1))
    finally:
        file.close()


def read_sequence(filename):
    try:
        file = open(filename, mode='rt', encoding='utf-8')
        return [int(line.strip()) for line in file]
    finally:
        file.close()


def main(filename, num):
    write_sequence(filename, num)
    print(read_sequence(filename))


if __name__ == '__main__':
    main(filename=sys.argv[1], num=int(sys.argv[2]))
