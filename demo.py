from edges import Undirected

ed = Undirected({})
ed.add('a','b')
ed.add('b','c')
ed.add('a','m')
print(ed.count())
# 3
print(ed.list())
# [['a', 'b'], ['a', 'm'], ['b', 'c']]
