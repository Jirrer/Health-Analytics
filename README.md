# Michigan Analytics

Website for graphing health and income trends per county in Michigan

# Backend
## Python Source Files
### What is their use?
The Python scripts handle all the data reading and procressing needs required by the API, and are split into three main .py files (with Methods\.py holding shared functionality). 

### Methods\.py
Methods\.py is used by all three of the main source files and is intended for abstracting logic for shared methods. Another feature for the source code is the Methods\.py handles all (most) external api calls and database queries. This allows for the three main .py files to focus on the custom data structures and code architecture. Functions within Methods\.py have a stand alone use and should not rely any helper functions, though many may call other functions within Methods\.py. Because of this, there is no function ording layout and the most recently created method simply gets put at the top. 

### Test\.py

### CalucateData\.py

### PullData\.py

### ScrapData\.py

## Requirements
 * beautifulsoup4\==4.14.3
 * blinker\==1.9.0
 * certifi\==2025.11.12
 * charset-normalizer\==3.4.4
 * click\==8.3.1
 * colorama\==0.4.6
 * Flask\==3.1.2
 * flask-cors\==6.0.2
 * idna\==3.11
 * itsdangerous\==2.2.0
 * Jinja2\==3.1.6
 * MarkupSafe\==3.0.3
 * numpy\==2.4.0
 * pandas\==2.3.3
 * pip\==24.0
 * python-dateutil\==2.9.0.post0
 * pytz\==2025.2
 * requests\==2.32.5
 * setuptools\==65.5.0
 * six\==1.17.0
 * soupsieve\==2.8.1
 * typing_extensions\==4.15.0
 * tzdata\==2025.3
 * urllib3\==2.6.2
 * Werkzeug\==3.1.4

# API

# Frontend

## Requirements