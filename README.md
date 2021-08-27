<p align="center">
  <img width="500" height="500" src="https://user-images.githubusercontent.com/74840026/131065667-34f697a3-fc66-4203-b728-549848c5dd8e.png">
</p>

# Mission_to_Mars

# Overview
Automate a browser to scrape multiple sites to extract data and images (`Beautifulsoup, Splinter`).  Once extracted, storing the info in a NoSQL database (`MongoDB`).  Then using `Flask`, create a web application to display the data and images.

## Languages and tools used:
- HTML
- MongoDB
- Python
    - Pandas
    - Beautifulsoup
    - Splinter
    - Flask
    - PyMongo
- Bootstrap

## Sites used:
[NASA Mars News](https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest)

[Space Images](https://spaceimages-mars.com/)

[Mars Facts](https://galaxyfacts-mars.com/)

[Mars Hemisphere](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)

# Process
1. Scraping.py
    - Beautifulsoup and Splinter; drill down into the HTML tags to extract the most recent news artile and summary from Mars News site
    - Beautifulsoup and Splinter; drill down into the HTML tags to extract the most recent image from Space Images site
    - Pandas; scrape Mars/Earth table and read as DataFrame then convert into HTML from Mars Facts site
    - Beautifulsoup and Splinter; drill down into the HTML tags to extract all four full size hemisphere images from Mars Hemisphere site
    - Store scraped data in MongoDB database
2. App.py
    - create app to connect MongoDB through Flask to set up web page
3. Index.html
    - create containers to display news article, images and table
    - create 'Scrape New Data' button to perform our scraping function
    - refactor code to ensure data displayed is responsive to multiple device sizes
    - Bootstrap; customize web page apprearance

# Summary
Our Flask app displays the most recent article scraped from the NASA Mars News site, an updated image from the Space Images site and a table from the Mars Facts site.  Four hemisphere images scraped from the Mars Hemisphere site are displayed at the bottom.  The page is responsive to desktops, tablets and phones.
![127 0 0 1_5000_ (1)](https://user-images.githubusercontent.com/74840026/130889013-120c28c9-d436-457c-8721-5fbae8e033a2.png)
