
import scrapy


class GMarket2Item(scrapy.Item):
    Name = scrapy.Field()
    Price = scrapy.Field()
    URL = scrapy.Field()