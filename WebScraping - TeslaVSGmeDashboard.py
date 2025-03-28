#WebScraping - TeslaVSGmeDashboard


!pip install yfinance
!pip install bs4
!pip install nbformat
!pip install --upgrade plotly
!pip install html5lib #important for html5lib parser and use of read_html, if we are using BeautifuSoupa and parser at all
!pip install lxml==4.6.4 #important for html5lib parser and use of read_html,if we are using BeautifuSoupa and parser at all

import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import plotly.io as pio
pio.renderers.default = "iframe"

import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    #fig.show() #if this is not under comment, two sets of same graphs will be displayed
    from IPython.display import display, HTML
    fig_html = fig.to_html()
    display(HTML(fig_html))

#Tesla historic data
tesla=yf.Ticker('TSLA')
tesla_data=tesla.history(period='max').reset_index()


#Tesla revenue data
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm'
tesla_revenue=pd.read_html(url, match='Tesla Quarterly Revenue',flavor='bs4')[0] #this may not work without html5lib as a parser, if we are using html instead of url,which we are not
tesla_revenue.rename(columns={'Tesla Quarterly Revenue (Millions of US $)': 'Date', 'Tesla Quarterly Revenue (Millions of US $).1': 'Revenue'}, inplace=True)
tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace('$',"") #remove $ sign
tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',',"") #remove , sign
tesla_revenue['Revenue']=tesla_revenue['Revenue'].astype(float) #cast Revenue from object to float
tesla_revenue['Date']=pd.to_datetime(tesla_revenue['Date'])
tesla_revenue.isnull().sum()#there is 1 null value in Revenue column
tesla_revenue.dropna(inplace=True)#drop the row with null value


#gme historic data
gme=yf.Ticker('GME')
gme_data=gme.history(period='max').reset_index()


#gme revenue data
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html'
gme_revenue=pd.read_html(url,match='GameStop Quarterly Revenue',flavor='bs4')[0]
gme_revenue.rename(columns={'GameStop Quarterly Revenue (Millions of US $)': 'Date', 'GameStop Quarterly Revenue (Millions of US $).1': 'Revenue'}, inplace=True)
gme_revenue['Revenue']=gme_revenue['Revenue'].str.replace('$',"") #remove $ sign
gme_revenue['Revenue']=gme_revenue['Revenue'].str.replace(',',"") #remove , sign
gme_revenue['Revenue']=gme_revenue['Revenue'].astype(float) #cast Revenue from object to float
gme_revenue['Date']=pd.to_datetime(gme_revenue['Date'])

make_graph(tesla_data, tesla_revenue, 'TESLA')
make_graph(gme_data, gme_revenue, 'GME')


