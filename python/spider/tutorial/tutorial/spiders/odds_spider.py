import scrapy
import datetime


class QuotesSpider(scrapy.Spider):
    name = "odds"

    def start_requests(self):
        urls = [
            '''https://www.sportsbook.ag/sbk/sportsbook4/golf-betting/2018-fort-worth-invitational-odds-to-win.sbk''',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for odds in response.css('div.eventrow'):
            yield {
                odds.css("span.team::text").extract_first(): {
                    "date": datetime.datetime.today(),
                    "odds": odds.css("div.market::text").extract_first(),
                }
            }
            # yield {
            #     "name": odds.css("span.team::text").extract_first(),
            #     "odds": odds.css("div.market::text").extract_first(),
            #     "date": datetime.datetime.today()
            # }
