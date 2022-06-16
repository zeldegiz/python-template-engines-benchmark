# python template engines benchmark
Template engines is very important things in web frameworks. In this repository, we calculate django template, flask template and jinja2 template engine speed.
## Results

|Number of Render|Django Template|Flask Template|Jinja2 from Disk| Jinja2 from String|
|--|--|--|--|--|
|100|2.05499 sec|0.12277 sec|0.04692 sec|0.03775 sec|
|250|4.15439 sec|0.28805 sec|0.11593 sec|0.06901 sec|
|500|8.24436 sec|0.56999 sec|0.24742 sec|0.13151 sec|
|1000|16.29227 sec|1.15499 sec|0.48573 sec|0.26959 sec|
