[CONTENIDO]
import scrapy
from scrapy.crawler import CrawlerProcess
from itemadapter import ItemAdapter
import psycopg2

class Page(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()

def run(url, output_db='ai_link_genius'):
    process = CrawlerProcess({
        'ITEM_PIPELINES': {
            'web_crawler.Pipeline': 300,
        },
        'FEEDS': {
            f'sqlite:///{output_db}.db?tables=pages&create_table=True': {'format': 'sql'}
        }
    })

    process.crawl(CrawlWebsiteSpider, start_urls=[url])
    process.start()

class CrawlWebsiteSpider(scrapy.Spider):
    name = "crawl_website"
    
    def __init__(self, start_urls=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = start_urls or []

    def parse(self, response):
        page = Page()
        page['url'] = response.url
        page['title'] = response.css('title::text').get()
        page['content'] = ' '.join(response.xpath('//p//text()').extract())
        
        yield page

class Pipeline:
    @classmethod
    def from_crawler(cls, crawler):
        return cls()

    def open_spider(self, spider):
        self.connection = psycopg2.connect(
            dbname="ai_link_genius", 
            user=os.environ['POSTGRES_USER'], 
            password=os.environ['POSTGRES_PASSWORD'],
            host='localhost'
        )
        self.cursor = self.connection.cursor()
        
    def close_spider(self, spider):
        self.cursor.close()
        self.connection.commit()
        self.connection.close()

    def process_item(self, item, spider):
        sql = "INSERT INTO pages (url, title, content) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (
            ItemAdapter(item).asdict()['url'],
            ItemAdapter(item).asdict()['title'], 
            ItemAdapter(item).asdict()['content']
        ))
        
        return item