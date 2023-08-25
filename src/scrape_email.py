from bs4 import BeautifulSoup
import requests
 
# Making a GET request
r = requests.get('https://www.linkedin.com/in/leo-park-a86a12288/')
data=r.json()
# check status code for response received
# success code - 200
print(data)
 
# print content of request
