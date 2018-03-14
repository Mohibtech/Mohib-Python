from scrapy.selector import Selector
import requests

# Urdu Novel Posts Link
response = requests.get("https://www.urduweb.org/mehfil/threads/%D9%88%DB%81-%D8%AC%D9%88-%D9%82%D8%B1%D8%B6-%D8%B1%DA%A9%DA%BE%D8%AA%DB%92-%D8%AA%DA%BE%DB%92-%D8%AC%D8%A7%D9%86-%D9%BE%D8%B1-%D8%A7%D8%B2-%D9%81%D8%B1%D8%AD%D8%AA-%D8%A7%D8%B4%D8%AA%DB%8C%D8%A7%D9%82-%D9%85%DA%A9%D9%85%D9%84-%D9%86%D8%A7%D9%88%D9%84.6032/")
selector = Selector(response)

summaries = selector.xpath('//div[@class="messageContent"]/article')
summaries[0]

msgText = [x.extract() for x in summaries.xpath('blockquote/text()')]

for m in msgText:
    print(m.strip())
