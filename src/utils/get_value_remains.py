def generate_list(numbers):
    for number in numbers:
        value_remains = get_value_remains(number)
        if len(value_remains) > 0:
            yield {number: value_remains}


def get_value_remains(number: int):
    array_good = []

    if number % 3 == 0:
        array_good.append("Марко")

    if number % 5 == 0:
        array_good.append("Поло")

    return ', '.join(array_good)
