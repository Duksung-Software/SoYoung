import scrapy
from G_market2.items import GMarket2Item

search = input('상품명을 입력하세요 : ')
URL = ['https://browse.gmarket.co.kr/search?keyword='+search]
        
arrange = input('상품 정렬 방식을 입력하세요 ( G마켓랭크순, 판매인기순, 낮은가격순, 높은가격순, 상품평많은순, 신규상품순 ) : ')

if (arrange=='G마켓랭크순'):
    pass
if (arrange=='판매인기순'):
    arrange_type=8
if (arrange=='낮은가격순'):
    arrange_type=1
if (arrange=='높은가격순'):
    arrange_type=2
if (arrange=='상품평많은순'):
    arrange_type=13
if (arrange=='신규상품순'):
    arrange_type=3

URL = ['https://browse.gmarket.co.kr/search?keyword='+search+ '&f=d:f&s='+str(arrange_type)]
class GMarket2Spider(scrapy.Spider):

    name = 'g_market2'
    start_urls = [URL]

    def parse(self, response):

        global url
        
        for i in range(1,101):

            URL = response.xpath(f'//*[@id="section__inner-content-body-container"]/div[2]/div[{i}]/div/div[2]/div[1]/div[1]/span/a')
            div =  response.xpath(f'//*[@id="section__inner-content-body-container"]/div[2]/div[{i}]')

            if (URL !=[]):
                href = div.xpath('./div/div[2]/div[1]/div[1]/span/a/@href')
                url = response.urljoin(href[0].extract())
                yield scrapy.Request(url, callback = self.page_content1)    
            
            if (URL ==[]):
                href = div.xpath('./div/div[2]/div[1]/div[2]/span/a/@href')
                url = response.urljoin(href[0].extract())
                yield scrapy.Request(url, callback = self.page_content2)

    def page_content1(self, response):
        item = GMarket2Item()
        item['Name'] = response.xpath('//*[@id="itemcase_basic"]/div[1]/h1/text()')[0].extract()
        item['Price'] = response.xpath('//*[@id="itemcase_basic"]/div[1]/p/span/strong/text()')[0].extract()
        item['URL'] = url
        return item

    def page_content2(self, response):
        item = GMarket2Item()
        item['Name'] = response.xpath('//*[@id="itemcase_basic"]/div[1]/h1/text()')[0].extract()
        item['Price'] = response.xpath('//*[@id="itemcase_basic"]/div[1]/p/span/strong/text()')[0].extract()
        item['URL'] = url
        return item