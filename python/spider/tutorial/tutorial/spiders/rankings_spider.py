import scrapy
import datetime


class QuotesSpider(scrapy.Spider):
    name = "rankings"

    def start_requests(self):
        urls = [
            'http://www.owgr.com/ranking',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for ranking in response.css('table>tr'):
            yield {
                "name": ranking.css("td.name a::text").extract_first(),
                "rank": ranking.css("td::text")[0].extract(),
                "last_week": ranking.css("td::text")[1].extract(),
                "2017": ranking.css("td::text")[2].extract(),
                "date": datetime.datetime.today()
            }

    def parse_golfer(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        yield {

        }
