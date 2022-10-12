# Mission_to_Mars

## Project Overview
The most recent Mars news, featured Mars images and facts, and high resolution images of each of Mars' Hemispheres, is scraped from 4 urls using splinter and beautiful soup. This data is stored with MongoDB and served to a webapp using Flask. The Flask webapp features all the information and images collected in the database, as well as a button triggering a new scrape. The button is linked to a second route which executes a new scrape, updates the MongoDB holding the site data, then redirects the browser back to the home route now featuring the updated data. 

### Resources
- Data Source: 'https://marshemispheres.com/', 'https://galaxyfacts-mars.com', 'https://spaceimages-mars.com', 'https://redplanetscience.com'
- Software: Python 3.7.1, Bootstrap 3.3.7, Flask 1.1.2, Splinter 0.18.1, BeautifulSoup4 4.11.1, MongoDB 6.0.2, webdriver-manager 3.8.3, VS Code 1.71.2

