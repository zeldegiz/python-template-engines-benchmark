# python template engines benchmark
Template engines is very important things in web frameworks. In this repository, we calculate django template, flask template and jinja2 template engine speed.
## Results

|Number of Render|Django Template|Flask Template|Jinja2 from Disk| Jinja2 from String|
|--|--|--|--|--|
|100|2.05499|0.12277|0.04692|0.03775|
|250|4.15439|0.28805|0.11593|0.06901|
|500|8.24436|0.56999|0.24742|0.13151|
|1000|16.29227|1.15499|0.48573|0.26959|
