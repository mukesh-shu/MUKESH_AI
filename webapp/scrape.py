import requests
import time
from bs4 import BeautifulSoup#beautyfullsoup4
#url store

url='http://54.225.7.146/'
#sendind the request
respond=requests.get(url)

if respond.status_code==200:
    print('succesfully')
    #chaking the status code
    time.sleep(2)
    print(respond.status_code)
    #activate html code
    time.sleep(2)
    print(respond.text)
    #html parsing 
    time.sleep(2)
    print("please wait my bs4 is doing parsing")
    parsed_data=BeautifulSoup(respond.text,'lxml')   # we have using lxml for parser but we can akso used html5

    #cheaking tag
    my_title=parsed_data.find('title')
       #cheaking tag
    my_title=parsed_data.find('title')
    if my_title:
        #for perticular to print title
        title_got=my_title.get_text()
        print("my title is",title_got)
    else:
        print('No title find in',url)


else :
    print('fail')