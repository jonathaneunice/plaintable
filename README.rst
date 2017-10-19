plaintable
==========

Plaintable is a simple library to build plain text tables. It has a clear,
Pythonic programming interface (API).

Some formatting attributes such as alignment, padding, and
floating point precision can be customized.

Usage
-----

.. code-block:: pycon

    >>> from plaintable import Table
    >>> data = [
    ...     [1, 2, 3, 4, 5],
    ...     [10, 11, 12, 13, 14],
    ...     ['a', 'b', 'c', 'd', 'e'],
    ...     [1.0, 2.0, 1.5, 4.25, 10.50],
    ... ]
    >>> headline = ['one', 'two', 'three', 'four', 'five']
    >>> table = Table(data, headline)
    >>> print(table)
    one   two   three  four  five
    ----  ----  -----  ----  -----
    1     2     3      4     5
    10    11    12     13    14
    a     b     c      d     e
    1.00  2.00  1.50   4.25  10.50


Customise
---------

The table layout can be customised by passing several keyword arguments
to ``Table.__init__()``.

headline
    A list of strings which will appear as column headers. This argument
    is optional.

    **Default: None**
truncate
    Tell plaintable to truncate columns which do not have any headline,
    see #8 for further information.

    **Default: True**
align
    You can specifiy the alignment of the table ('l', 'r', 'c').

    **Default: 'l'**
padding
    If you need a wider table you can increase the padding.

    **Default: 2**
floatprec
    Every float value is converted to ``str`` with this precision.

    **Default: 2**
header_padding
    Adds extra spaces around header fields.

    **Default: 0**
datetimefs
    Specifies the datetime formatstring. Any datetime object is converted
    to a string refering to this formatstring; see also here_.

    **Default:** ``%Y-%m-%d %H:%M``

.. _here: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior


Incremental Construction
------------------------

As of version 0.2, it is possible to incrementally construct a table. This is handy
if one is reading each line from a CSV file, say, or a database connection.

.. code-block:: pycon

    >>> from plaintable import Table
    >>> data = [
    ...     [1, 2, 3, 4, 5],
    ...     [10, 11, 12, 13, 14],
    ...     ['a', 'b', 'c', 'd', 'e'],
    ...     [1.0, 2.0, 1.5, 4.25, 10.50],
    ... ]
    >>> table = Table(headline=['one', 'two', 'three', 'four', 'five'])
    >>> for row in data:
    ...     table.append(row)
    >>> print(table)
    one   two   three  four  five
    ----  ----  -----  ----  -----
    1     2     3      4     5
    10    11    12     13    14
    a     b     c      d     e
    1.00  2.00  1.50   4.25  10.50

Existing tables can have data added to via ``append``, ``extend``, or ``insert``
operations, just like a Python ``list``. In fact, since table data is stored as
a list (in ``table.data``), any manipulation operations you can perform on a
list are possible, though only the most common ones are exposed as direct
``Table`` methods.

Table formatting is deferred until the moment a string representation of the
table is requested, e.g. through ``str(table)`` or ``print(table)``. One
consequence is that if you print a table, then add data and re-print, the column
widths may grow as subsequent prints accomodate wider data elements.


Further Examples
----------------

.. code-block:: pycon

    >>> from plaintable import Table
    >>> data = [
    ...    [1, 2, 3, 4, 5],
    ...    [10, 11, 12, 13, 14],
    ...    ['a', 'b', 'c', 'd', 'e'],
    ...    [1.0, 2.0, 1.5, 4.25, 10.50],
    ... ]
    >>> headline = ['one', 'two', 'three', 'four', 'five']
    >>> table = Table(data, headline, align='r', padding=4, floatprec=4)
    >>> print(table)
           one       two     three      four       five
        ------    ------    ------    ------    -------
             1         2         3         4          5
            10        11        12        13         14
             a         b         c         d          e
        1.0000    2.0000    1.5000    4.2500    10.5000


.. code-block:: pycon

    >>> from plaintable import Table
    >>> data = [
    ...    [1, 2, 3, 4, 5],
    ...    [10, 11, 12, 13, 14],
    ...    ['a', 'b', 'c', 'd', 'e'],
    ...    [1.0, 2.0, 1.5, 4.25, 10.50],
    ... ]
    >>> table = Table(data)
    >>> print(table)
    1     2     3     4     5
    10    11    12    13    14
    a     b     c     d     e
    1.00  2.00  1.50  4.25  10.50


.. code-block:: pycon

    >>> from plaintable import Table
    >>> data = [
    ...    [1, 2, 3, 4, 5],
    ...    [10, 11, 12, 13, 14],
    ...    ['a', 'b', 'c', 'd', 'e'],
    ...    [1.0, 2.0, 1.5, 4.25, 10.50],
    ... ]
    >>> table = Table(data, padding=4)
    >>> print(table)
    1       2       3       4
    10      11      12      13
    a       b       c       d
    1.00    2.00    1.50    4.25


.. code-block:: pycon

    >>> from plaintable import Table
    >>> data = [
    ...    [1, 2, 3, 4, 5],
    ...    [10, 11, 12, 13, 14],
    ...    ['a', 'b', 'c', 'd', 'e'],
    ...    [1.0, 2.0, 1.5, 4.25, 10.50],
    ... ]
    >>> table = Table(data, header_padding=4)
    >>> print(table)
    one          two          three          four
    -----------  -----------  -------------  ------------
    1            2            3              4
    10           11           12             13
    a            b            c              d
    1.00         2.00         1.50           4.25
