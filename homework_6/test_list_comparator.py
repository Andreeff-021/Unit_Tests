import pytest
from list_comparator import ListComparator


def test_compare_lists():
    lc = ListComparator([1, 2, 3], [4, 5, 6])
    assert lc.compare_lists() == "Второй список имеет большее среднее значение"

    lc = ListComparator([4, 5, 6], [1, 2, 3])
    assert lc.compare_lists() == "Первый список имеет большее среднее значение"

    lc = ListComparator([1, 2, 3], [1, 2, 3])
    assert lc.compare_lists() == "Средние значения равны"


if __name__ == '__main__':
    pytest.main(['-v'])
