def float_parser(number : str):
    try:
        number = float(number)
    except ValueError:
        return False
    return number