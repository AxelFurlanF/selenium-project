from selenium import webdriver
from secrets import url

MIN_PAGE = 219
MAX_PAGE = 290

FIRST_FILTER_MAX = 650
FIRST_FILTER_MIN = 400


class SearchBot:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.run()

    def run(self):
        with open('results.csv', 'a+') as f:
            pages = range(MAX_PAGE, MIN_PAGE, -1)
            for page in pages:
                self.driver.get(url.format(page=page))
                names, videos, views, urls = self.users_per_page()

                for idx, views_count in enumerate(views):
                    if "K" in views_count and "." not in views_count and self.first_conditional(views_count[:-1]):
                        f.write('{0},{1},{2},{3}\n'.format(names[idx], views[idx], videos[idx], urls[idx]))

    def users_per_page(self):
        # user name
        sel_users = self.driver.find_elements_by_xpath('//a[@class="title js-mxp"]')
        names = [name.text for name in sel_users if name.text != '']

        # user videos, views
        sel_info = self.driver.find_elements_by_xpath('//span[@class="videosNumber"]')
        list_info = [data.text for data in sel_info]
        videos_count = [int(video[:2]) for video in list_info]
        views_count = [views[views.find('Videos ') + 7: views.find(' views')] for views in list_info]

        # user url
        sel_url = self.driver.find_elements_by_xpath('//a[@class="title js-mxp"]')
        urls = [url.get_attribute("href") for url in sel_url]

        return names, videos_count, views_count, urls

    def first_conditional(self, count):
        return FIRST_FILTER_MIN <= int(count) <= FIRST_FILTER_MAX


bot = SearchBot()
