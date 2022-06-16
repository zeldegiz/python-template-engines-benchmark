from jinja2 import Environment, FileSystemLoader
import time


env = Environment(loader=FileSystemLoader("./templates"))
template = env.get_template("index.html")
values = {'mystring': 'Hello World', 'ls': [*range(1000)]}

t = time.time()

for i in range(500):
    template.render(**values)

print(time.time()-t)