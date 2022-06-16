from jinja2 import Template

template = Template('''<!DOCTYPE html>
<html>
  <head>
    <title>Template Engine Test</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css" rel="stylesheet" media="screen">
  </head>
  <body>
  <p>Input String: {{my_string}}</p>

    {% for n in ls %}
    <p>{{n}}</p>
    {% endfor %}
  </ul>
  <h3> This is the end of my child template</h3>
  </body>
</html>''')