
BOT_NAME = 'G_market2'

SPIDER_MODULES = ['G_market2.spiders']
NEWSPIDER_MODULE = 'G_market2.spiders'

ROBOTSTXT_OBEY = False

LOG_FILE = 'G_market2.log'

FEED_EXPORT_FIELDS = "utf-8-sig"

FEED_EXPORT_FIELDS = ["Name","Price","URL"]

DUPEFILTER_CLASS = 'scrapy.dupefilters.BaseDupeFilter'