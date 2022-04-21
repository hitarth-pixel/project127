from selenium import webdriver as wd
from bs4 import BeautifulSoup as bs
import time as t
import csv as c

START_URL ="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=wd.Chrome("C:\class127\chromedriver")
browser.get(START_URL)
t.sleep(10)

def scrape():
    headers=["name","distance","mass","radius"]
    star_data=[]
    for i in range(0,97):
        soup=bs(browser.page_source,"html.parser")
        for ulTag in soup.find_all("ul",attrs={"class","starRecord"}):
            li_tags=ulTag.find_all("li")
            temp_list=[]
            for index,li_tag in enumerate(li_tags):
                if index==0:temp_list.append(li_tag.find_all("a")[0].content[0])
                else:
                    try:temp_list.append(li_tag.content[0])
                    except:temp_list.append("")
            star_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scrapper.csv","w") as f:
        csvwriter=c.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(star_data)
scrape()