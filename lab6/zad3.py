#!/usr/bin/python3
import itertools, functools,re,sys
data = itertools.chain(iter(open(sys.argv[1])), iter(open(sys.argv[2])))
data = re.findall(r'[0-9]+', functools.reduce(lambda a,e: a+e, iter(data)))
data = map(int, iter(data))
data = filter(lambda x: (x % 2) == 0 , iter(data) )
print(len(list(data)))

