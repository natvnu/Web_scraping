#Webscraping basics

!pip uninstall beautifulsoup4 -y #this is optional, used in case of a persistant error that pandas require newer version of bs4. Reinstall needed afterwards
!pip install beautifulsoup4
!mamba install bs4==4.10.0 -y
!pip install lxml==4.6.4
!mamba install html5lib==1.1 -y
!pip install pandas

!pip install requests==2.31.0

from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page


!pip install --upgrade beautifulsoup4
#!pip install --upgrade bs4

!pip install --upgrade pandas
#!pip3 install --upgrade pandas
import pandas as pd
import bs4 
print(bs4.__version__)


'''
#TAG OBJECTS soup.tag
html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
#parse html to a nested data structure instead of a string
soup = BeautifulSoup(html, "html.parser")
#print nested data structure in an easily readable way
#print(soup.prettify())
#define tag_object - the first h3
tag_object=soup.h3
print('tag object: ',tag_object)
#print parent object of h3 - body
tag_parent=tag_object.parent
print('tag parent: ',tag_parent)
#print sibling of h3 - p
tag_sibling1=tag_object.next_sibling
print('tag sibling: ',tag_sibling1)
#print child of of h3 - b
tag_child=tag_object.b
print('tag child: ',tag_child)
#content within the <> </>, type is navigable string (similar to string but with more features)
tag_string=tag_child.string 
print('navigable string: ',tag_string)

#ACCESING TAG'S ATTRIBUTES
tag_child['id'] #returns string 'boldest'
tag_child.get('id') #returns string 'boldest'
tag_child.attrs #returns dictionary {'id': 'boldest'}


#FILTERING HTML - find_all
#find_all(name, attrs, recursive, string, limit, **kwargs)
#html below is a table
html="<table><tr><td id='flight' >Flight No</td><td>Launch site</td><td>Payload mass</td></tr><tr><td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a> </td><td>80 kg</td></tr></table>"
soup=BeautifulSoup(html,'html.parser')
#print(soup.prettify())
#rows of the table, type is bs4.element.ResultSet, like a list
table_rows=soup.find_all('tr') #
print('Table rows: ',table_rows)
#first row, type bs4.element.Tag
first_row=table_rows[0]
print('First row: ',first_row)
#second row using index or using next_sibling
second_row=first_row.next_sibling
# or second_row=table_rows[1]
print('Second row: ',second_row)
#first row child (td), or first element of the first row type bs4.element.Tag
first_row_child=first_row.td
print('First element: ', first_row_child)
#row by row
for i, row in enumerate(table_rows):
    print('row',i,'is',row)
#a list of tr and td tags    
list_input=soup .find_all(name=["tr", "td"])
list_input
#Beautiful Soup will filter against each tag’s id attribute. For example, the first td elements have a value of id of flight, therefore we can filter based on that id value.
soup.find_all(id="flight")
#find all the elements that have links to the Florida Wikipedia page:
list_input=soup.find_all(href="https://en.wikipedia.org/wiki/Florida")
list_input
#find all links - not the best way
list_input=soup.find_all(href=True)
list_input
#find all tags that are not links
list_input=soup.find_all(href=False)
# find all tags with id='boldest'
list_input=soup.find_all(id='boldest')#it will be empty as there are no tags with id='boldest'
#With string we search for strings instead of tags, where we find all the elments with Florida:
list_input=soup.find_all(string='Florida')
list_input
#if we are looking for one element (not all) we can use the find

#TWO TABLES
two_tables="<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"
soup=BeautifulSoup(two_tables,'html.parser')
#print(soup.prettify())
#we can find the first table like this - create a list of tables and then search for the first one in the list
tables=soup.find_all('table')
first_table = tables[0]
#or we can find it by searching for the first table
first_table=soup.find('table')
#print('First table: ', first_table.prettify())#we can prettify any tag element
#we can find the second table like this - filtering the 'class' attribute 
second_table=soup.find("table",class_='pizza')
#we can also find it 
second_table=tables[1]
#but we cannot find it using first_table.next_sibling


#DOWNLOADING AND SCRAPING THE CONTENTS OF THE WEBPAGE
url = "https://web.archive.org/web/20230224123642/https://www.ibm.com/us-en/"
#download page using get method
r=requests.get(url) #pay attention not to use 'url', but to use it without quotes
#extract html from the page
html=r.text
#parse html using BeautifulSoup
soup=BeautifulSoup(html,'html.parser')
#print(soup.prettify())
#scrape all links and keep them in bs4.element.ResultSet
#links=soup.find_all('a')
#links
#better way to scrape all the links
for link in soup.find_all('a',href=True):  # in html anchor/link is represented by the tag <a>
    print(link.get('href'))
#scrape all images tags
for img in soup.find_all('img'):  # in html anchor/link is represented by the tag <a>
    print(img.get('src'))
#scrape all the tables -  there is only 1 actually
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
html=requests.get(url).text#we skipped one line in acquiring html
soup=BeautifulSoup(html,'html.parser')
#print(soup.prettify())
tables=soup.find_all('table')#in this case we have only one table
#get all rows from the table
table_rows=soup.find_all('tr')
table_rows
#iterate through bs4.element.ResultSet and print out the color name and the color code
df=pd.DataFrame(columns=['Name', 'Number'])
for row in (table_rows):
    #print(row)
    row_elements=row.find_all('td')
    print(row_elements[2].string) #prints color name
    print(row_elements[3].string)#prints color code
'''

#SCRAPE HTML TABLES (TAG OBJECTS) TO DATAFRAME USING LOOP - DATAFRAME CONSTRUCTION - SUPER IMPORTANT!!!!
url = "https://en.wikipedia.org/wiki/World_population"
html=requests.get(url).text
soup=BeautifulSoup(html,'html.parser')
tables=soup.find_all('table')
#we need to locate the table that represents 10 most densely populated countries on the webpage
i=-1#set i to -1 because indexing starts with 0, not with 1 (in which case we would set it to 0)
for table in tables:
    i=i+1#iterate index with every table in tables set
    if ("10 most densely populated countries" in str(table.caption)):#here we can use str(table) as well, in case we do not know under which tag is the title of the table
        index=i #store i in index var - so we know the index (aka location) of the table we are looking for
#print(tables[index].prettify())#print our table to see how it looks like
#create dataframe to store the table scraped from web page
top_10_df=pd.DataFrame(columns=['Rank', 'Country','Population', 'Area', 'Density'])
for row in tables[index].find_all('tr'):
    #print(row)
    cols=row.find_all('td')
    if cols:#this is necessary for the code below to work
        rank=cols[0].text.strip()#using .text.strip() instead of .string like previously removes unwanted \n
        country=cols[1].text.strip()
        pop=cols[2].text.strip()
        area=cols[3].text.strip()
        density=cols[4].text.strip()
        #create a temp data frame (which will consist of 1 row every iteration) and fill it with values
        df_temp=pd.DataFrame([{'Rank':rank, 'Country':country,'Population':pop, 'Area':area, 'Density':density}])
        #concat df_temp to df
        top_10_df = pd.concat([top_10_df, df_temp], ignore_index=True)
top_10_df#data frame of 10 ten countries


#IMPORT HTML TABLE (TAG OBJECT) TO DATAFRAME USING read_html and bs4- may report that we need newer bs4 version error 
#(which can be solved by uninstalling and installing bs4 as shown at the top of this file)
#using panda's read_html with string version of the table and the flavor which is the parsing engine bs4
list_df=pd.read_html(str(tables[6]), flavor='bs4')#read_html returns list of dataframes, we only want the first one
top_10_df=list_df[0]
top_10_df


#SCRAPE HTML TABLES DIRECTLY FROM URL TO DATAFRAME USING read_html
list_of_all_df_on_the_page=pd.read_html(url,flavor='bs4')
len(list_of_all_df_on_the_page)#there are 27 tables on this list
top_10_df=list_of_all_df_on_the_page[6]#1st WAY we know our table has index 6
#2nd WAY - OR we can search for the table with a certain title like below
top_10_df=pd.read_html(url, match="10 most densely populated countries", flavor='bs4')[0]
top_10_df



