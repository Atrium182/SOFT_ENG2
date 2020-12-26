# Scrapy settings for forecast_scrape project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'forecast_scrape'

SPIDER_MODULES = ['forecast_scrape.spiders']
NEWSPIDER_MODULE = 'forecast_scrape.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'forecast_scrape (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'forecast_scrape.middlewares.ForecastScrapeSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html

DOWNLOADER_MIDDLEWARES = {
   'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
   'forecast_scrape.middlewares.UserAgentRotatorMiddleware': 400,
   'rotating_proxies.middlewares.RotatingProxyMiddleware': 800,
   'rotating_proxies.middlewares.BanDetectionMiddleware': 800
}

<<<<<<< HEAD
# DOWNLOADER_MIDDLEWARES = {
#    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
#    'forecast_scrape.middlewares.UserAgentRotatorMiddleware': 400,
#    'rotating_proxies.middlewares.RotatingProxyMiddleware': 800,
#    'rotating_proxies.middlewares.BanDetectionMiddleware': 800
# }

# ROTATING_PROXY_LIST_PATH = 'proxies.txt'
=======
# ROTATING_PROXY_LIST_PATH = 'proxies.txt'
ROTATING_PROXY_LIST = {
   '78.138.131.248:3128',
   '83.103.193.74:13192',
   '161.202.226.194:8123',
   '187.44.167.78:60786',
   '149.202.222.94:3128',
   '163.53.209.7:6666',
   '54.38.33.2:80',
   '190.145.200.126:53281',
   '92.115.102.133:55443',
   '180.250.12.10:80'
}
>>>>>>> scraper

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'forecast_scrape.pipelines.ForecastScrapePipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

DB_SETTINGS = {
    'db':"forecast_db",
    'user':'root',
    'passwd':'',
    'host':'localhost'
}