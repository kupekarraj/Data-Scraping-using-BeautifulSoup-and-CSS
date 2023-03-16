#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#importing the necessary libraries
import requests
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[ ]:


#initialise the web driver
browser = webdriver.Chrome(ChromeDriverManager().install())


# In[ ]:


#Empty lists for appending the output data
Blog=[]
Link=[]
Date=[]


# In[ ]:


#creating a list of the input urls to iterate using a for loop
urls=["https://blog.avast.com/page/21","https://blog.avast.com/page/22"]


# In[ ]:


#looping to pull the data for multiple input urls
for i in urls:
    browser.get(i)
    #Check out page source code
    blog=browser.page_source
    #Use Beautiful Soup to get access tags
    blog_soup=bs(blog,'lxml')
    containers = blog_soup.find_all("div",{"class":"article-item article-item-medium span"})
    for container in containers:
        blog_container=container.find("div",{"class":"box"})
        blog_text=blog_container.find("h3").text
        blog_link=container.find("a",href=True)["href"]
        blog_published_date=container.find("span",{"class":"meta-added"}).text
        Blog.append(blog_text)
        Link.append(blog_link)
        Date.append(blog_published_date)


# In[ ]:


#creating a dataframe using the appended output lists
data = {
    "Blog": Blog,
    "Link": Link,
    "Date": Date
}

df = pd.DataFrame(data)


# In[ ]:


#displaying the top head of the dataframe
df.head(30)


# In[ ]:


#writing the output dataframe on a local machine
df.to_csv(r'your desired output path goes here', index=False)

