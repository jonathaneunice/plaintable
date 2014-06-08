from datetime import datetime
import plaintable
import pytest


data = [[1, 2, 3, 4],
        [10, 11, 12, 13],
        ['a', 'b', 'c', 'd'],
        [1.0, 2.0, 1.5, 4.25]]
dates = [[datetime(2000, 1, 1)],
         [datetime(1960, 2, 2)]]
headline = ['one', 'two', 'three', 'four']


def test_data_defaults():
    table = plaintable.Table(data)
    assert str(table) == ('1     2     3     4     \n'
                          '10    11    12    13    \n'
                          'a     b     c     d     \n'
                          '1.00  2.00  1.50  4.25  ')


def test_dates_defaults():
    table = plaintable.Table(dates)
    assert str(table) == ('2000-01-01 00:00  \n'
                          '1960-02-02 00:00  ')


def test_float_precision():
    table = plaintable.Table(data, floatprec=4)
    assert str(table) == ('1       2       3       4       \n'
                          '10      11      12      13      \n'
                          'a       b       c       d       \n'
                          '1.0000  2.0000  1.5000  4.2500  ')
