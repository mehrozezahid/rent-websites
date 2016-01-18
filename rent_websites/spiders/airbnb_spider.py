from scrapy.spiders import Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from rent_websites.spiders.RentBaseSpider import RentBaseSpider
from rent_websites.items import PlaceItem


class AirbnbSpider(RentBaseSpider):
    name = "airbnb"
    allowed_domains = ["airbnb.com"]
    start_urls = ["https://www.airbnb.com/sitemaps"]

    rules = (
        Rule(SgmlLinkExtractor(restrict_xpaths=("//*[@class='sitemap']//a",
                                                ))),
        Rule(SgmlLinkExtractor(restrict_xpaths=("//*[@class='next next_page']/a",
                                                ))),
        Rule(SgmlLinkExtractor(restrict_xpaths=("//*[@itemprop='name']/a",
                                                )),
             callback="parse_product"),
    )

    def parse_product(self, response):
        """Function extracting values from product page"""

        item = PlaceItem()
        item['item_source'] = response.url
        item['name'] = self.get_name(response)
        item['price'] = self.get_price(response)
        yield item

    def get_name(self, response):
        return response.xpath("//*[@id='listing_name']/text()").extract()[0]

    def get_price(self, response):
        return response.xpath("//*[contains(@class,'book-it__price-amount')]//text()").extract()[0].strip()
