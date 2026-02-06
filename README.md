# Michigan Analytics
##### Quick Nav Links
[Backend](#backend) | [API](#api) | [Frontend](#frontend) | [Database](#database) | [Python Requirements](#python-requirements)

Full stack application for calculating, storing, and showcasing health & income within the counties of the state of the Michigan. Its frontend allows the user to select (either click on the map or search for) a county and the api will send the selected data. The user can decide the number of data points (types of information) for each query.   

# Backend
## Python Source Files
### What is their use?
The Python scripts handle all the data reading and procressing needs required by the API, and are split into three main .py files (with Methods\.py holding shared functionality). 

### Methods\.py
Methods\.py is used by all three of the main source files and is intended for abstracting logic for shared methods. Another feature for the source code is the Methods\.py handles all (most) external api calls and database queries. This allows for the three main .py files to focus on the custom data structures and code architecture. Functions within Methods\.py have a stand alone use and should not rely any helper functions, though many may call other functions within Methods\.py. Because of this, there is no function ording layout and the most recently created method simply gets put at the top. 

### ScrapData\.py
ScrapeData is at the forefront of the backend. It is the methods within this file's job to pull the essiential information needed for the data within the database. Any and all scrape functions can be called (selected from the corrisponding .txt file) at any time. These functions are a variety of webscrapers, public API calls, or plain CSV proccessors. Once this data is verified, it can be used in other parts of the codebase 

### CalculateData\.py
It is CalculateData's job to process and calculate the data that gets sent to the database. After using data pulled form the ScrapeData methods, the raw information is calculated into short numbers that represent rankings, percentages, ratios, etc. These numbers can be chosen to be sent to the database.

Available Calculations
* GiniCoeffient(year: int)
* Deaths()

### PullData\.py
PullData acts as an abstraction layer for pulling information from the database. It is the methods in this file that the API uses to get its information. 

# API

# Python Requirements
 * annotated-types\==0.7.0
 * anyio\==4.9.0
 * asgiref\==3.7.2
 * beautifulsoup4\==4.14.3
 * blinker\==1.9.0
 * build\==1.3.0
 * cachetools\==5.5.2
 * certifi\==2025.11.12
 * charset-normalizer\==3.4.4
 * click\==8.3.1
 * colorama\==0.4.6
 * contourpy\==1.3.3
 * customtkinter\==5.2.2
 * cycler\==0.12.1
 * darkdetect\==0.8.0
 * distro\==1.9.0
 * Django\==5.0.1
 * docopt\==0.6.2
 * dotenv\==0.9.9
 * Flask\==3.1.2
 * flask-cors\==6.0.2
 * fonttools\==4.61.1
 * google-ai-generativelanguage\==0.6.15
 * google-api-core\==2.24.2
 * google-api-python-client\==2.166.0
 * google-auth\==2.38.0
 * google-auth-httplib2\==0.2.0
 * google-generativeai\==0.8.4
 * googleapis-common-protos\==1.69.2
 * grpcio\==1.71.0
 * grpcio-status\==1.71.0
 * h11\==0.14.0
 * httpcore\==1.0.7
 * httplib2\==0.22.0
 * httpx\==0.28.1
 * idna\==3.11
 * image\==1.5.33
 * iniconfig\==2.3.0
 * itsdangerous\==2.2.0
 * Jinja2\==3.1.6
 * jiter\==0.9.0
 * Js2Py\==0.74
 * kiwisolver\==1.4.9
 * MarkupSafe\==3.0.3
 * matplotlib\==3.10.8
 * mysql-connector\==2.2.9
 * mysql-connector-python\==9.2.0
 * numpy\==2.4.0
 * openai\==1.72.0
 * packaging\==25.0
 * pandas\==2.3.3
 * pillow\==12.1.0
 * pip\==24.0
 * pluggy\==1.6.0
 * proto-plus\==1.26.1
 * protobuf\==5.29.4
 * pyasn1\==0.6.1
 * pyasn1_modules\==0.4.2
 * pydantic\==2.11.3
 * pydantic_core\==2.33.1
 * pygame\==2.6.1
 * Pygments\==2.19.2
 * pyjsparser\==2.7.1
 * pyparsing\==3.3.1
 * pypdf\==6.1.3
 * PyPrind\==2.11.3
 * pyproject_hooks\==1.2.0
 * pySmartDL\==1.3.4
 * pytest\==9.0.2
 * pytest-mock\==3.15.1
 * python-dateutil\==2.9.0.post0
 * python-dotenv\==1.1.0
 * python_helper\==0.3.74
 * pytz\==2025.2
 * redis\==5.2.1
 * requests\==2.32.5
 * rsa\==4.9
 * scipy\==1.16.1
 * setuptools\==65.5.0
 * six\==1.17.0
 * sniffio\==1.3.1
 * soupsieve\==2.8.1
 * spotipy\==2.25.1
 * sqlparse\==0.4.4
 * tqdm\==4.67.1
 * typing_extensions\==4.15.0
 * typing-inspection\==0.4.0
 * tzdata\==2025.3
 * tzlocal\==5.3.1
 * uritemplate\==4.1.1
 * urllib3\==2.6.2
 * vermin\==1.7.0
 * Werkzeug\==3.1.4
# Frontend
## React
## Charts
# Database
