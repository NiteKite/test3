# -*- coding: utf-8 -*-
from scrapy import Spider


class TwitterFollowersSpider(Spider):
    name = 'twitter_followers'
    allowed_domains = ['twitter.com']
    twitter_handle = input('\nEnter Twitter handle (excluding "@"): ')
    start_urls = [f'https://twitter.com/{twitter_handle}']

    def parse(self, response):
        name = response.xpath('//h1[@class="ProfileHeaderCard-name"]/a/text()').extract_first()
        followers = response.xpath('//a[@data-nav="followers"]/span[@class="ProfileNav-value"]/@data-count').extract_first()

        yield {'Name': name, 'Handle': f'@{self.twitter_handle}', 'Followers': int(followers)}