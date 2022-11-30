import sys,re,functools
from collections import Counter
dane = re.findall(r"\S+", sys.stdin.read())
dane = str(dict(Counter((map(lambda i:len(i), dane)))))
print(dane)
