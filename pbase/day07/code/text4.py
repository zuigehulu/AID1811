from collections import namedtuple
doc = namedtuple('doc',['name','age','jobs'])
bob = doc('bob',age=12,jobs = 'asdf')
print(bob)
oo = bob._asdict()
print(oo)