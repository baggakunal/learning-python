
def nth_root(radicand: int, n: int) -> float:
    return radicand ** (1/n)


def ordinal_suffix(value: int) -> str:
    s = str(value)

    if s.endswith('11'):
        return 'th'
    elif s.endswith('12'):
        return 'th'
    elif s.endswith('13'):
        return 'th'
    elif s.endswith('1'):
        return 'st'
    elif s.endswith('2'):
        return 'nd'
    elif s.endswith('3'):
        return 'rd'
    else:
        return 'th'


def ordinal(value: int) -> str:
    return str(value) + ordinal_suffix(value)


def display_nth_root(radicand: int, n: int) -> None:
    root: float = nth_root(radicand, n)
    message: str = "The " + ordinal(n) + " root of " + str(radicand) + " is " + str(root)
    print(message)
