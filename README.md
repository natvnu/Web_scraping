# Web_scraping

The repository contains:
1. WebScraping - TeslaVSGmeDashboard.py - Tesla VS GME import of historical stock data using yfinance. Import of revenue data from table scraped from a webpage using read_html(match table title). Visual representation of both for both Tesla and GME.
2. NETFLIX - WebScraping.py - Netflix import of historical stock data using yfinance. Import of data from table scraped from a webpage using find_all and a loop and using read_html.
3. Webscraping basics.py Web_scraping basics - downloading html through Requests and parsing through BeautifulSoup, searching for tag objects, searching for tables, use of read_html and bs4.

Dataset Sources: 
1.  Macrotrends stocks data https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm (originally from: https://www.macrotrends.net/stocks/charts/tsla/tesla/revenue)
2.  Yahoo finance stocks data https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html (originally from: Netflix, Inc. (NFLX) Stock Price, News, Quote & History - Yahoo Finance)
3.  HTML data available from IBM course "Python Project for Data Science" (https://www.coursera.org/learn/python-project-for-data-science/home/module/1)


Technologies Used: Python, Pandas, BeautifuLSoup, Requests, yfinance, IPython
Installation: copy and run the code in Jupyter Notebooks or other Python editor of choice.

Example of results:

![Tesla Historical Share Price](tesla_historical_share_price.png)


![Tesla Historical Revenue](tesla_historical_revenue.png)


![Netflix Historical Stocks Data - Scraping tables in 4 ways](Netflix_historical_data.png)


![Tag_objects](Tag_objects.png)


![Most Densely Populated Countries - Scraping tables to df using loop](Most_densely_populated_countries_scraping_tables_to_df_using_loop.png)


![Most Densely Populated Countries - Scraping tables to df using directly from url using read_html and bs4](Most_densly_populated_countries_scrape_tables_to_df_directly_from_url_using_read_html_and_bs4.png)




