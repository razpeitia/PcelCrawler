# -*- coding: utf-8 -*-

# Scrapy settings for Pcel project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'Pcel'

SPIDER_MODULES = ['Pcel.spiders']
NEWSPIDER_MODULE = 'Pcel.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Pcel (+http://www.yourdomain.com)'

AUTOTHROTTLE_ENABLED = True
