# -*- coding: utf-8 -*-
import urllib.request
import re
import time
import os
from selenium import webdriver
import sys

abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
os.chdir(dname)

def downloadPinterestImages():
    link="https://www.pinterest.es/metdaan/art"
    limit=20 #limit of scrolls    
    browser = webdriver.Firefox(executable_path=r'geckodriver.exe')
    browser.get(link)
    time.sleep(2)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
    while(match==False and limit>0): #auto scroll till end or till limit
        lastCount = lenOfPage
        time.sleep(3)
        lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        limit = limit-1;
        if lastCount==lenOfPage:
            print("stop scrolling")
            match=True
        else:
            print("scrolling..")

    response = browser.page_source#.encode(encoding='UTF-8')

    toDel =[]
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', response)

    print(len(urls))
    for i in range(len(urls)):
        #abc=urls[i][0:24]
        if(urls[i][0:25]=="https://i.pinimg.com/474x"):
            urls[i]="https://i.pinimg.com/564x"+urls[i][25:]
        else:
            urls[i]= ""

    urls = list(set(urls))

    urls = list(filter(None, urls)) # fastest
    urls = list(filter(bool, urls)) # fastest
    urls = list(filter(len, urls))  # a bit slower

    with open('raw.txt', 'w') as f:
        for url in urls:
            f.write("%s\n" % url)
    f.close()

    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, os.path.basename(link))
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)

    for i in range(len(urls)):
        my_string=urls[i]
        abc=os.path.basename(my_string)
        try:
            urllib.request.urlretrieve(urls[i], os.path.basename(link)+"/"+abc)
        except:
            print("Broken Link") 

downloadPinterestImages()
