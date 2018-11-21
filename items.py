import scrapy

class CrawlerItem(scrapy.Item):
    #define the fields for your item here, such as:
    # name = scrapy.Field()
    title = scrapy.Field()
    email = scrapy.Field()
    comments = scrapy.Field()
    form = scrapy.Field()
    location_url = scrapy.Field()
