# Test 3 Scraper README

This is the repository for the third interview test.

In involves creating a web scraper that scrapes a Twitter account's number of followers based on an input.

This repository includes two versions of the scraper: one using the Scrapy framework (taking about 15 minutes to write), and one using requests and BeautifulSoup (taking about 35 minutes to write -- some brushing-up necessary).

For this exercise, I assume that I should not be using the Twitter API (also, I do not have a Twitter account)

The Scrapy version can be run through command line:

"scrapy runspider twitter_followers_a.py" or 

"scrapy runspider twitter_followers_a.py -o items.csv" for csv output.

Learning how to actually push the code to Github took less than 10 minutes, however this was supplemented with about 2 hours of learning about what Git is and how to use it locally. 

* Note: Scrapy does not seem to be supported in Python 3.7 yet.