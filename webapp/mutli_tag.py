import requests
import time
from bs4 import BeautifulSoup#beautyfullsoup4
#url store

url='http://54.225.7.146/'
#sendind the request
respond=requests.get(url)

if respond.status_code==200:
    print('succesfully')

    # #chaking the status code
    # time.sleep(2)
    # print(respond.status_code)

    # #activate html code
    # time.sleep(2)
    # print(respond.text)
    # time.sleep(2)

    #html parsing 
    print("please wait my bs4 is doing parsing")
    parsed_data=BeautifulSoup(respond.text,'lxml')   # we have using lxml for parser but we can akso used html5

    #cheaking tag
    #my_title=parsed_data.find('title')
    my_data=parsed_data.find_all('l1')
    if my_data:
        for item in my_data:
            
            print("my title is",item.get_text())
    else:
        print('No title find in',url)

else :
    print('you need to rechake the url')