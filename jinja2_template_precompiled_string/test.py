from templates import *
import time

values = {'mystring': 'Hello World', 'ls': [*range(1000)]}

t = time.time()

for i in range(500):
    template.render(**values)

print(time.time()-t)