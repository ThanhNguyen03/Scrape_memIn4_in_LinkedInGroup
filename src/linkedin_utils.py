from time import sleep

from parsel import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import parameters

import requests
from bs4 import BeautifulSoup
import re


def get_chrome_driver():
    # options = webdriver.EdgeOptions()
    # options.add_argument('headless')
    driver = webdriver.Chrome(ChromeDriverManager().install())

    return driver

def login_user(args, driver):
    driver.get(parameters.URLS['login'])
    username = driver.find_element(By.ID,'username')
    username.send_keys(args.email)
    sleep(0.5)

    password = driver.find_element(By.ID,'password')
    password.send_keys(args.password)
    sleep(0.5)

    sign_in_button = driver.find_element(By.XPATH,'//*[@type="submit"]')
    sign_in_button.click()
    sleep(0.5)


def get_urls_of_group_members(group_ids, driver):
    profile_urls = list()
    group_ids = group_ids.split(',')

    for group_id in group_ids:
        driver.get(parameters.URLS['group'].format(group_id.strip()))
        sleep(3)
        group_profile_urls = driver.find_elements(By.CLASS_NAME,'ui-entity-action-row__link')
        profile_urls += [url.get_attribute('href') for url in group_profile_urls]
        sleep(0.5)
    return profile_urls

# def get_url_contact(driver):
    
#     # driver.get(profile_url)
#     # sleep(5)
#     # for profile_url in tqdm(profile_urls):
#     #     driver.get(profile_url)
#     #     sleep(5)
#     #     member_contact_urls = driver.find_elements(By.CLASS_NAME,'ember-view link-without-visited-state')
#     #     contact_urls += [url.get_attribute('href') for url in member_contact_urls]
#     member_contact_urls = driver.find_element(By.CLASS_NAME,'ember-view link-without-visited-state')
#     contact_urls = str([url.get_attribute('href') for url in member_contact_urls])
#     sleep(3)
#     driver.get('https://www.linkedin.com/'+contact_urls)
#     sleep(5)
#     sel=Selector(text=driver.page_source)

#     contact = sel.xpath('//*[@class = "pv-profile-section__section-info section-info"]')
#     email_contact = contact.xpath('//*[@class = "pv-contact-info__contact-type ci-email"]')
#     if email_contact==None: email = "None"
#     else: email = email_contact.xpath('//a[@class = "pv-contact-info__contact-link"]//span/text()').extract_first()
#     sleep(0.5)

#     return email



# def scrape_profiles(driver, profile_urls):
    # members =[]
    # #contact_urls=list()
    # i=0
    # for profile_url in tqdm(profile_urls):
    #     member = dict()
    #     driver.get(profile_url)
    #     sleep(5)
    #     sel = Selector(text=driver.page_source)

        # member['name'] = ''.join(
        #     sel.xpath('//*[@class = "text-heading-xlarge inline t-24 v-align-middle break-words"]/text()').extract_first())
        # member['url'] = driver.current_url
        # member['position'] = ' '.join(
        #     sel.xpath('//*[@class = "mt1 t-18 t-black t-normal"]/text()').extract_first().split(','))
        # experience = sel.xpath('//*[@class = "pv-top-card--experience-list"]')
        # company = experience.xpath('.//a[@data-control-name = "position_see_more"]//span/text()').extract_first()
        # member['company'] = ''.join(company.split(',')) if company else None
        # education = experience.xpath('.//a[@data-control-name = "education_see_more"]//span/text()').extract_first()
        # member['education'] = ' '.join(education.split(',')) if education else None
        # member['location'] = ' '.join(
        #     sel.xpath('//*[@class = "t-16 t-black t-normal inline-block"]/text()').extract_first().split(','))
        #contact = sel.xpath('//*[@class = "pv-contact-info__ci-container t-14"]')

        # sel_1=get_url_contact(profile_url,driver)

        # email_contact = sel_1.xpath('//*[@class = "pv-contact-info__contact-type ci-email"]')
        # email = email_contact.xpath('//a[@class = "pv-contact-info__contact-link"]//span/text()').extract_first()
    #     member['email'] = ''.join(email) if email else None
        
    #     members+=member
    #     i+=1
    #     if i>5: break
    # return members

def getdata(url): 
    r = requests.get(url) 
    return r.text

def scrape_profiles(driver, profile_url):
    member = dict()
    driver.get(profile_url)
    sleep(5)
    sel = Selector(text=driver.page_source)

    member['name'] = ''.join(
        sel.xpath('//*[@class = "text-heading-xlarge inline t-24 v-align-middle break-words"]/text()').extract_first())
    sleep(0.5)
    member['url'] = driver.current_url
    sleep(0.5)
    member['position'] = ''.join(
        sel.xpath('//*[@class = "text-body-medium break-words"]/text()').extract_first().strip().replace(",",";"))
    
    profile = profile_url + "/overlay/contact-info/"
    driver.get(profile)
    sc = driver.page_source
    email = re.findall('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',sc)


    member['email'] = ''.join(email) if email else None 
    
    return member


