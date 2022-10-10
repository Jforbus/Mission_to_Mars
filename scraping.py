# import dependencies
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt



#############################################################
## Main Function
#############################################################

# define function to initialize headless browser and execute all scraping functions
def scrape_all():

    # initialize headless splinter browser
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    # assign variables to outputs of article function for seperate storage
    news_title, news_paragraph = mars_news(browser)

    # run remaining scraping functions and store all data in dictionary
    data = {
      "news_title": news_title,
      "news_paragraph": news_paragraph,
      "featured_image": featured_image(browser),
      "facts": mars_facts(),
      "last_modified": dt.datetime.now()}
    
    # close browser
    browser.quit()

    return data



#############################################################
## Subordinate Functions
#############################################################

# define article scraping function
def mars_news(browser):

    # assign and visit URL
    url = 'https://redplanetscience.com'
    browser.visit(url)

    #  confirm element presence, delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # build HTML parser, parse URL
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # try/except for error handling during scraping
    try:

        # select target element
        slide_elem = news_soup.select_one('div.list_text')

        # filter element for newest article title
        news_title = slide_elem.find('div', class_='content_title').get_text()

        # filter element for newest article summary
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
    
    except AttributeError:
        
        return None, None

    return news_title, news_p




# define image scraping function
def featured_image(browser):

    # visit URL
    i_url = 'https://spaceimages-mars.com'
    browser.visit(i_url)

    # find and click full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # parse the  html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # try/except for error handling during scraping
    try:

        # find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    
    except AttributeError:
        
        return None


    # concatenate image url
    img_url = f'{i_url}/{img_url_rel}'

    return img_url




# define fact table scraping function
def mars_facts():

    # try/except for error handling during scrape
    try:
            
        # use pandas to read table HTML
        df = pd.read_html('https://galaxyfacts-mars.com')[0]
    
    except BaseException:
        return None

    # Assign Columns and set index
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)

    # convert DatatFrame back to HTML
    return df.to_html(classes="table table-striped")

if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())





