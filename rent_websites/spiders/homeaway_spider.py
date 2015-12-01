from scrapy.spiders import Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from rent_websites.spiders.RentBaseSpider import RentBaseSpider
from rent_websites.items import PlaceItem


class HomeawaySpider(RentBaseSpider):
    name = "homeaway"
    allowed_domains = ["homeaway.com"]
    start_urls = ['https://www.homeaway.com/vacation-rentals/malaysia/r42']

    rules = (
        Rule(SgmlLinkExtractor(restrict_xpaths=("(//*[@class='region-refinement'])[1]",
                                                "//*[@class='next']/a"
                                                ))),

        Rule(SgmlLinkExtractor(restrict_xpaths=("//*[@class='hit-content']//*[@class='hit-headline']//a",
                                                )),
             callback="parse_product"),
    )

    def parse_product(self, response):
        print("In parse_product")

        item = PlaceItem()
        item['name'] = self.get_name(response)
        item['price'] = self.get_price(response)
        yield item

    def get_name(self, response):
        return response.xpath("(//*[@class='container hidden-phone']//h1/text())").extract()[0]

    def get_price(self, response):
        return response.xpath("(//*[@class='price-large']/text())").extract()[0]
