from utils.get_value_remains import generate_list, get_value_remains


def test_generate_list():
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    num_good = [3, 6, 9, 12, 15, 18, 5, 10, 20]
    for value in generate_list(num_list):
        keys = list(value.keys())[0]
        assert keys in num_good


def test_get_value_remains_good():
    value = get_value_remains(3)
    assert value == "Марко"
    value = get_value_remains(5)
    assert value == "Поло"
    value = get_value_remains(15)
    assert value == "Марко, Поло"


def test_get_value_remains_error():
    value = get_value_remains(1)
    assert len(value) == 0
    value = get_value_remains(2)
    assert len(value) == 0
    value = get_value_remains(4)
    assert len(value) == 0
    value = get_value_remains(6)
    assert len(value) == 0
