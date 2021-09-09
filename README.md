<p align="center">
  <img width="500" height="500" src="https://user-images.githubusercontent.com/74840026/131065667-34f697a3-fc66-4203-b728-549848c5dd8e.png">
</p>

# Mission_to_Mars

# Overview
Automate a browser to scrape multiple sites to extract data and images (`Beautifulsoup, Splinter`).  Once extracted, storing the info in a NoSQL database (`MongoDB`).  Then using `Flask`, create a web application to display the data and images.

## Languages and tools used:
<img align="left" alt="HTML" width="56px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/html/html.png" />
<img align="left" alt="Python" width="56px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" />
<img align="left" alt="Bootstrap" width="56px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/bootstrap/bootstrap.png" />
<img align="left" alt="MongoDB" width="56px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/mongodb/mongodb.png" />
<img align="left" alt="Flask" width="56px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/flask/flask.png" />
<img align="left" alt="Visual Studio Code" width="56px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/visual-studio-code/visual-studio-code.png" /> 
<br/>
<br/>
<br/>

- Pandas
- Beautifulsoup
- Splinter
- PyMongo
<br\>

## Sites used:
[NASA Mars News](https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest)

[Space Images](https://spaceimages-mars.com/)

[Mars Facts](https://galaxyfacts-mars.com/)

[Mars Hemisphere](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)

# Process
1. Scraping.py
    - Beautifulsoup and Splinter; drill down into the HTML tags to extract the most recent news article and summary from Mars News site
    - Beautifulsoup and Splinter; drill down into the HTML tags to extract the most recent image from Space Images site
    - Pandas; scrape Mars/Earth table and read as DataFrame then convert into HTML from Mars Facts site
    - Beautifulsoup and Splinter; drill down into the HTML tags to extract all four full size hemisphere images from Mars Hemisphere site
    - Store scraped data in MongoDB database

<p align="center">
  <img src="https://user-images.githubusercontent.com/74840026/131202176-161d6380-9554-4ca1-848e-9541c5d27259.PNG">
</p>

2. App.py
    - create app to connect MongoDB through Flask to set up web page
3. Index.html
    - create containers to display news article, images, and table
    - create 'Scrape New Data' button to perform our scraping function
    - refactor code to ensure data displayed is responsive to multiple device sizes
    - Bootstrap; customize web page appearance(background color change, jumbotron image fill, button color change, text color change)

# Summary
Our Flask app displays the most recent article scraped from the NASA Mars News site, an updated image from the Space Images site and a table from the Mars Facts site.  Four hemisphere images scraped from the Mars Hemisphere site are displayed at the bottom.  The page is responsive to desktops, tablets, and phones.

![127 0 0 1_5000_ (1)](https://user-images.githubusercontent.com/74840026/130889013-120c28c9-d436-457c-8721-5fbae8e033a2.png)

# 
#### Contact
E-mail: boyerjason700@gmail.com
