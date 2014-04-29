import plaintable

data = [[1, 2, 3, 4, 5], [10, 11, 12, 13, 14], ['a', 'b', 'c', 'd', 'e'], [1.0, 2.0, 1.5, 4.25, 10.50]]
headline = ['eins', 'zwei', 'drei', 'vier', 'fünf']
table = plaintable.Table(data)
table2 = plaintable.Table(data, headline, align='l', padding=4, floatprec=4)
print(table)
print()
print(table2)
