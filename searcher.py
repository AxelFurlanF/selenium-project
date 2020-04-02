from selenium import webdriver 
from time import sleep
from secrets import url
import pandas as pd

class search_bot:
    def __init__(self):
        # self.df = pd.DataFrame()
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()  # importante, sino esta maximizado oculta algunos perfiles
        # final_list = run()
        sleep(2)
        
    def run(self):
        pages = range(290, 219, -1)
        for page in pages:
            pass
        pass    
        
    def users_per_page(self):
        # user name
        sel_users = self.driver.find_elements_by_xpath('//a[@class="title js-mxp"]')
        names = [name.text for name in sel_users if name.text != '']
        
        
        # user videos, views
        sel_info = self.driver.find_elements_by_xpath('//span[@class="videosNumber"]')
        list_info = [data.text for data in sel_info]
        videos_count = [int(video[:2]) for video in list_info]
        views_count = [views[views.find('Videos ') + 7 : views.find(' views')] 
                       for views in list_info]

        # user url
        sel_url = self.driver.find_elements_by_xpath('//a[@class="title js-mxp"]')
        urls = [url.get_attribute("href") for url in sel_url] 
        
        return names, videos_count, views_count, urls 
    
    
    def first_conditional(self, profile_information):
        pass
    

    
    def save_all(self, sel_obj):
        pass
    
       
    def previous_page(self):
        self.driver.find_element_by_xpath('//li[@class="page_previous alpha"]')\
            .click()        
         
        
        

        
        
        
        
bot = search_bot()
names, videos, views, urls = bot.users_per_page()

    # def check_gender(self, gender_information):
    #     # window_before = driver.window_handles[0]
    #     # window_after = driver.window_handles[1]
    #     # driver.switch_to.window(window_after)
    #     pass
