import requests
from lxml import html


class Fridge(object):
    
    def __init__(self, main_url):
        self.links = []
        self.main_url = main_url

    def get_page_limit(self):
        response = requests.get(self.main_url)
        tree = html.fromstring(response.text)
        dirty_link = tree.xpath('//*[@id="feed-panel-wrapper"]/div[7]/div[2]/a[5]/@href')
        self.link_limit = dirty_link[0][:-5]

    def get_single_title(self, url):
        response = requests.get(url)
        tree = html.fromstring(response.text)
        cufs = tree.xpath('//div[@class="post-content"]/div/h2/text()')
        try:
            print cufs[0]
        except UnicodeEncodeError:
            print cufs[0].encode('utf-8')
        except IndexError:
            pass

    def get_page_data(self, page_num):
        if page_num == 1:
            page = ''
        else:
            page = '/page/{}/'.format(page_num)
        page_url = '{}{}'.format(self.main_url, page)
        response = requests.get(page_url)
        tree = html.fromstring(response.text)
        pathX = ('//div[@class="inner"]/div[@class="article-image"]'
                    '/a[@class="darken"]/@href')
        links = tree.xpath(pathX)
        for link in links:
            self.get_single_title(link)
