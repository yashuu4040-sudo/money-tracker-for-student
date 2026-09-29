def valid_amount(amount):
    return amount > 0


def valid_choice(choice, minimum, maximum):
    try:
        number = int(choice)
        return minimum <= number <= maximum
    except ValueError:
        return False
