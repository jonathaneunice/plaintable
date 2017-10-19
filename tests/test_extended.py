from datetime import datetime
import plaintable
import pytest


data = [
    [1, 2, 3, 4],
    [10, 11, 12, 13],
    ['a', 'b', 'c', 'd'],
    [1.0, 2.0, 1.5, 4.25],
]
headline = ['one', 'two', 'three', 'four']


def test_incremental():

    table = plaintable.Table()
    for row in data:
        table.append(row)
    assert str(table) == (
        '1     2     3     4\n'
        '10    11    12    13\n'
        'a     b     c     d\n'
        '1.00  2.00  1.50  4.25'
    )
    table.headline = headline
    assert str(table) == (
        'one   two   three  four\n'
        '----  ----  -----  ----\n'
        '1     2     3      4\n'
        '10    11    12     13\n'
        'a     b     c      d\n'
        '1.00  2.00  1.50   4.25'
    )


def test_data_append():
    table = plaintable.Table(data)
    assert str(table) == (
        '1     2     3     4\n'
        '10    11    12    13\n'
        'a     b     c     d\n'
        '1.00  2.00  1.50  4.25'
    )
    assert len(table) == 4
    table.append([5, 10, 20, 40])
    assert len(table) == 5
    assert str(table) == (
        '1     2     3     4\n'
        '10    11    12    13\n'
        'a     b     c     d\n'
        '1.00  2.00  1.50  4.25\n'
        '5     10    20    40'
    )
    table.append(['1', '22', '666666', '333'])
    assert len(table) == 6
    assert str(table) == (
        '1     2     3       4\n'
        '10    11    12      13\n'
        'a     b     c       d\n'
        '1.00  2.00  1.50    4.25\n'
        '5     10    20      40\n'
        '1     22    666666  333'
    )
    # note column size change
    table.headline = headline
    assert str(table) == (
        'one   two   three   four\n'
        '----  ----  ------  ----\n'
        '1     2     3       4\n'
        '10    11    12      13\n'
        'a     b     c       d\n'
        '1.00  2.00  1.50    4.25\n'
        '5     10    20      40\n'
        '1     22    666666  333'
    )
    assert len(table) == 6


def test_data_extend():
    table = plaintable.Table(data)
    assert str(table) == (
        '1     2     3     4\n'
        '10    11    12    13\n'
        'a     b     c     d\n'
        '1.00  2.00  1.50  4.25'
    )
    assert len(table) == 4
    table.extend([[5, 10, 20, 40],
                  ['1', '22', '666666', '333']])
    assert str(table) == (
        '1     2     3       4\n'
        '10    11    12      13\n'
        'a     b     c       d\n'
        '1.00  2.00  1.50    4.25\n'
        '5     10    20      40\n'
        '1     22    666666  333'
    )
    assert len(table) == 6
    table.headline = headline
    assert str(table) == (
        'one   two   three   four\n'
        '----  ----  ------  ----\n'
        '1     2     3       4\n'
        '10    11    12      13\n'
        'a     b     c       d\n'
        '1.00  2.00  1.50    4.25\n'
        '5     10    20      40\n'
        '1     22    666666  333'
    )
    assert len(table) == 6


def test_data_insert():
    table = plaintable.Table(data)
    assert str(table) == (
        '1     2     3     4\n'
        '10    11    12    13\n'
        'a     b     c     d\n'
        '1.00  2.00  1.50  4.25'
    )
    assert len(table) == 4
    table.insert(0, [5, 10, 20, 40])
    assert len(table) == 5
    assert str(table) == (
        '5     10    20    40\n'
        '1     2     3     4\n'
        '10    11    12    13\n'
        'a     b     c     d\n'
        '1.00  2.00  1.50  4.25'
    )
    table.insert(2, ['1', '22', '666666', '333'])
    assert len(table) == 6
    table.headline = headline
    assert str(table) == (
        'one   two   three   four\n'
        '----  ----  ------  ----\n'
        '5     10    20      40\n'
        '1     2     3       4\n'
        '1     22    666666  333\n'
        '10    11    12      13\n'
        'a     b     c       d\n'
        '1.00  2.00  1.50    4.25'
    )
    assert len(table) == 6
