plaintable
==========

Plaintable is a very simple library to build plain text tables. It has been 
created to provide a very lightweight and clear interface for generating plain 
text tables. Some data can be customized e.g. alignment, padding and floatprecision.
Every data item is to be converted to string automatically.


Usage
-----

Data with headline

.. code-block:: pycon

    >>> from plaintable import Table
    >>> data = [[1, 2, 3, 4, 5], 
    ...         [10, 11, 12, 13, 14], 
    ...         ['a', 'b', 'c', 'd', 'e'], 
    ...         [1.0, 2.0, 1.5, 4.25, 10.50]]
    >>> headline = ['one', 'two', 'three', 'four', 'five']
    >>> table = Table(data, headline)
    >>> print(table)
    one   two   three  four  five   
    ----  ----  -----  ----  -----  
    1     2     3      4     5      
    10    11    12     13    14     
    a     b     c      d     e      
    1.00  2.00  1.50   4.25  10.50

Data without headline

.. code-block:: pycon

     >>> from plaintable import Table
     >>> data = [[1, 2, 3, 4, 5], 
     ...         [10, 11, 12, 13, 14], 
     ...         ['a', 'b', 'c', 'd', 'e'], 
     ...         [1.0, 2.0, 1.5, 4.25, 10.50]]
     >>> table = Table(data)
     >>> print(table)
     1     2     3     4     5      
     10    11    12    13    14     
     a     b     c     d     e      
     1.00  2.00  1.50  4.25  10.50


Customise
---------

The table layout can be customised by passing several keyword arguments
to ``Table.__init__``.

align
    You can specifiy the alignment of the table ('l', 'r', 'c'). 
    **Default: 'l'**
padding
    If you need a wider table you can increase the padding. 
    **Default: 2**
floatprec
    Every float value is converted to ``str`` with this precision.
    **Default: 2**


Further Examples
----------------

.. code-block:: pycon

    >>> from plaintable import Table
    >>> data = [[1, 2, 3, 4, 5],
    ...         [10, 11, 12, 13, 14], 
    ...         ['a', 'b', 'c', 'd', 'e'],
    ...         ['a', 'b', 'c', 'd', 'e'],
    ...         [1.0, 2.0, 1.5, 4.25, 10.50]]
    >>> headline = ['one', 'two', 'three', 'four', 'five']
    >>> table = Table(data, headline, align='r', padding=4, floatprec=4)
    >>> print(table)
           one       two     three      four       five
        ------    ------    ------    ------    -------
             1         2         3         4          5
            10        11        12        13         14
             a         b         c         d          e
        1.0000    2.0000    1.5000    4.2500    10.5000

