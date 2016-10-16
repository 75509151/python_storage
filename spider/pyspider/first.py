from pyspider.libs.base_handler import *


class Handler(BaseHandler):
    clawl_config = {}

    @every(minutes=60)
    def on_start(self):
        self.crawl('http://scrapy.org', callback=self.index_page)

    @config(age=60 * 60)
    def index_page(self, response):
        for each in response.doc('a[href^="http"]').items():
            self.crawl(each.attr.href, callback=self.detail_page)

    def detail_page(self, response):
        return {
            "url": response.url,
            "titile": response.doc('title').text(),
        }
