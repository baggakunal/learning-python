from math import sqrt

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def main():
    print([n for n in range(101) if is_prime(n)])


if __name__ == '__main__':
    main()
