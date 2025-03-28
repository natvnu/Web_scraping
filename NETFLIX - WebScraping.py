#NETFLIX - WebScraping


!pip install pandas
!pip install requests
!pip install bs4
!pip install html5lib 
!pip install lxml
!pip install plotly
!pip install yfinance
#import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup

import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)
'''
#Historic data about Netflix are available below
netflix = yf.Ticker("NFLX")
df_netflix_history=netflix.history(period='max').reset_index()
df_netflix_history[df_netflix_history['Date']=='2021-06-01 00:00:00-04:00']
'''
#Historic data about Netflix are available above, but our task is to scrape the table into df using BS
#1. Send an HTTP request to the web page using the requests library.
#2. Parse the HTML content of the web page using BeautifulSoup.
#3. Identify the HTML tags that contain the data you want to extract.
#4. Use BeautifulSoup methods to extract the data from the HTML tags.
#5. Print the extracted data

url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html'
html=requests.get(url).content #1

soup=BeautifulSoup(html,'html.parser')#2
#print(soup.prettify())


#1st way - NESTED LOOP - MY WAY
#find all tables in html
tables=soup.find_all('table')

#scrape column headers for df we will construct
column_headers=[]
for column in tables[0].find_all('th'):
    column_headers.append(column.string)
column_headers #will use this later

#create a netflix df 
netflix_df=pd.DataFrame()
#for all rows in the html table
for row in (tables[0].find_all('tr')):
    #print(row.string)
    #create a temp row list to store elements
    temp_row=[]
    #for every element of the row
    for el in row.find_all('td'):
        #print(el.string)
        #store it in the temp row list
        temp_row.append(el.string)
    #print(temp_row)
    #create a temp dataframe, filled with elements of the row (df will contain inly 1 row)
    df_temp=pd.DataFrame(temp_row).transpose() #will need to transpose the df to have data as a row, not a col
    #print(df_temp)
    #concatenate temp_df to netflix_df
    netflix_df = pd.concat([netflix_df, df_temp], ignore_index=True) 
#assign column headers to netflix df
netflix_df.columns=column_headers
netflix_df

#2nd way - IMPORT HTML TABLE (TAG OBJECT) TO DATAFRAME USING read_html and bs4
our_table=pd.read_html(str(tables[0]), flavor='bs4')#read_html returns a list of dataframes with one df only 
netflix_df=our_table[0]
netflix_df

#3rd way - SCRAPING HTML PAGE DIRECTLY FROM HTML TO DATAFRAME USING read_html and bs4
list_of_all_df_on_the_page=pd.read_html(html,flavor='bs4')#instead of html we can use url
netflix_df=list_of_all_df_on_the_page[0]
netflix_df

#4th way - SINGLE LOOP - THEIR WAY
netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])
# First we isolate the body of the table which contains all the information
# Then we loop through each row and find all the column values for each row
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    
    # Finally we append the data of each row to the table

    netflix_data = pd.concat([netflix_data,pd.DataFrame({"Date":[date], "Open":[Open], "High":[high], "Low":[low], "Close":[close], "Adj Close":[adj_close], "Volume":[volume]})], ignore_index=True)    
print('NEFLIX - historical data')
netflix_data.head()

