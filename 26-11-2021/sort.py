n = {'anu': 40, 'achu': 2, 'bob': 1, 'benny': 3}

l = list(n.items())

l.sort()
print('Ascending order is', l)

l = list(n.items())
l.sort(reverse=True)
print('Descending order is', l)
