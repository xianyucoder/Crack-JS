import cfscrape

# 实例化一个CloudflareScraper对象
scraper = cfscrape.create_scraper()
# 或者scraper = cfscrape.CloudflareScraper()也可以
# 如果出现错误可以加个延迟
# scraper = cfscrape.create_scraper(delay = 10)
# 获取真实网页源代码
web_data = scraper.get("https://wallhere.com/").content
print(web_data)

# pip install cfscrape
# 处理post的CloudFlare
# import cfscrape
# 实例化一个CloudflareScraper对象
# scraper = cfscrape.create_scraper()
# 或者scraper = cfscrape.CloudflareScraper()也可以
# 如果出现错误可以加个延迟
# scraper = cfscrape.create_scraper(delay = 10)
# 获取真实网页源代码
# web_data = scraper.post("http://example.com").content

