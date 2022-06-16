from flask import Flask, render_template
import time
app = Flask(__name__)

@app.route('/')
def index():
    values = {'mystring': 'Hello World', 'ls': [*range(1000)]}
    t = time.time()
    for i in range(500):
        render_template('index.html',**values)
    return str(time.time()-t)
    
if __name__ == '__main__':
    app.run()