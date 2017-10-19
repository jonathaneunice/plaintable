from plaintable import Table

print('Standard Usage')
print('======== =====')
print()

data = [
	[1, 2, 3, 4, 5],
	[10, 11, 12, 13, 14],
	['a', 'b', 'c', 'd', 'e'],
	[1.0, 2.0, 1.5, 4.25, 10.50],
]
headline = ['one', 'two', 'three', 'four', 'five']
table = Table(data, headline)
print(table)

print()
print()

print('Extended Usage')
print('======== =====')
print()

print('orig len:', len(table))

import math
new_row = [121.21, math.pi, math.e, -9.9999999, math.sqrt(2)]
table.append(new_row)
print('new len: ', len(table))
print()

print(table)

print()
print()


print('Incremental Construction')
print('=========== ============')
print()

data2 = [
	[1, 2, 3, 4, 5],
	[10, 11, 12, 13, 14],
	['a', 'b', 'c', 'd', 'e'],
	[1.0, 2.0, 1.5, 4.25, 10.50],
	[121.21, math.pi, math.e, -9.9999999, math.sqrt(2)],
]

table2 = Table(headline=['one', 'two', 'three', 'four', 'five'])
for row in data2:
	table2.append(row)
print(table2)

print()
print()
