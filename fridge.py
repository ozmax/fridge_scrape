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
        print cufs[0]

    def loop_pages(self):
        page = 1
        print 'page {}'.format(page)
        page_url = self.main_url
        while True:
            response = requests.get(page_url)
            tree = html.fromstring(response.text)
            pathX = ('//div[@class="inner"]/div[@class="article-image"]'
                     '/a[@class="darken"]/@href')
            links = tree.xpath(pathX)
            self.links.extend(links)
            if page_url == self.link_limit:
                break
            page += 1
            page_url = '{}/page/{}/'.format(self.main_url, page)
    
    def loop_links(self):
        for link in self.links:
            self.get_single_title(link)
