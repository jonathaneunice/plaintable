from plaintable import Table
data = [
	[1, 2, 3, 4, 5],
    [10, 11, 12, 13, 14],
    ['a', 'b', 'c', 'd', 'e'],
    [1.0, 2.0, 1.5, 4.25, 10.50],
]
headline = ['one', 'two', 'three', 'four', 'five']
table = Table(data, headline)
print(table)
