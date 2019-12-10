# GeoforAll Members Map

This is program which generates a map of the existing GeoforAll members.

Requirements
------------
* Python 2   https://www.python.org/downloads/  
* virtualenv https://pypi.org/project/virtualenv/

How to run
-----------
1. Install above programs and navigate to app/  
2. Execute ```source bin/activate``` in shell to activate.  
3. (Optional) Run generate.py to generate a new dataset from the website.  
4. Execute ```python -m SimpleHTTPServer 8000```.  
5. Open a web browser and goto http://localhost:8000  
6. Execute ```deactivate``` in shell to exit the virtualenv.  

How this was developed
--------
First, I looked up about Leaflet since that was my choice for creating the map. After I found that geojson was used for it I looked up how to create geojson from python. That's where I found the ```geojson``` library for Python. Then I used ```urllib3``` and ```beautifulsoup4``` to scrape the data from the web page (Some coordinates are faulty I think). Then that dataset was used to generate the map.
