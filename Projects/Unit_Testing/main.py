def add(a, b):
    return a + b


def smallest_factor(n):
    if n == 1:
        return 1
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            return i
    return n


def month_length(month, leap_year=False):
    if month in {"September", "April", "June", "November"}:
        return 30
    elif month in {"January", "March", "May", "July",
                   "August", "October", "December"}:
        return 31
    if month == "February":
        if not leap_year:
            return 28
        else:
            return 29
    else:
        return None


def operate(a, b, oper):
    if type(oper) is not str:
        raise TypeError("oper must be a string")
    elif oper == '+':
        return a + b
    elif oper == '-':
        return a - b
    elif oper == '*':
        return a * b
    elif oper == '/':
        if b == 0:
            raise ZeroDivisionError("division by zero is undefined")
        return int(a / b)
    raise ValueError("oper must be one of '+', '/', '-', or '*'")
