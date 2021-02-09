import scrapy
import time
from tqdm import tqdm

class DomofondFlatsSpider(scrapy.Spider):
    name = 'domofond_flats'
    allowed_domains = ['www.domofond.ru']
    
    urls_list = []
    for i in range(1,1964+1):
        urls_list.append('https://www.domofond.ru/prodazha-kvartiry-sankt_peterburg-c3414?SortOrder=Newest&Page={}'.format(i))
    
    start_urls = urls_list
    base_url = 'https://www.domofond.ru/'

    def parse(self, response):
        print("procesing page: "+ response.url[86:])
        urls = response.xpath(".//a[@class='long-item-card__item___ubItG search-results__itemCardNotFirst___3fei6']/@href").extract()
        
        for url in urls:
            yield scrapy.Request(response.urljoin(url), callback=self.parse_flat)
    
    def parse_flat(self, response):
        
        # Иногда при парсинге запрос возвращал пустые данные, из-за чего выдавал ошибку.
        # Добавил try/except, чтобы повторять запрос до тех пор пока данные не будут получены.ы
        try:
            print("procesing flat: "+ response.url)
            # Собираем информацию
            # Тип
            flat_type = response.xpath("//div[@class='detail-information__row___29Fu6']/span[2]").extract()[0]       
            # Тип объекта
            object_type = response.xpath("//div[@class='detail-information__row___29Fu6']/span[2]").extract()[1]        
            # Комнаты
            rooms = response.xpath("//div[@class='detail-information__row___29Fu6']/span[2]").extract()[2]       
            # Этажы
            floors = response.xpath("//div[@class='detail-information__row___29Fu6']/span[2]").extract()[3]
            # Площадь
            square = response.xpath("//div[@class='detail-information__row___29Fu6']/span[2]").extract()[4]
            # Площадь кухни
            kitchen_square = response.xpath("//div[@class='detail-information__row___29Fu6']/span[2]").extract()[5]
            # Жилая площадь
            live_square = response.xpath("//div[@class='detail-information__row___29Fu6']/span[2]").extract()[6]
            # Цена
            price = response.xpath("//div[@class='detail-information__row___29Fu6']/span[2]").extract()[7]
            # Цена за м2
            price_per_m = response.xpath("//div[@class='detail-information__row___29Fu6']/span[2]").extract()[8]
            # Материал здания
            build_matireal = response.xpath("//div[@class='detail-information__row___29Fu6']/span[2]").extract()[9]
            # Дата публикации объявления
            public_date = response.xpath("//div[@class='detail-information__row___29Fu6']/span[2]").extract()[10]
            # Дата обновления объявления
            update_date = response.xpath("//div[@class='detail-information__row___29Fu6']/span[2]").extract()[11]
            # Номер в каталоге
            catalog_id = response.xpath("//div[@class='detail-information__row___29Fu6']/span[2]").extract()[12]
            # Рейтинг района
            district_rating = response.xpath("//div[@class='area-rating__ratingNumber___1XZ04']/text()").extract()
            # Метро
            underground = response.xpath("//div[@class='information__metro___2zFqN']/text()").extract()

            # создать словарь для хранения извлеченной информации
            scraped_info = {
                  'page': response.url,
                  'flat_type': flat_type, 
                  'object_type': object_type,
                  'rooms': rooms,
                  'floors': floors,
                  'square': square,
                  'kitchen_square': kitchen_square,
                  'live_square': live_square,
                  'price': price,
                  'price_per_m': price_per_m,
                  'build_matireal': build_matireal,
                  'public_date': public_date,
                  'update_date': update_date,
                  'catalog_id': catalog_id,
                  'district_rating': district_rating,
                  'underground' : underground
                }
            
            yield scraped_info
            
        except IndexError:
            print('Retrying...')
            yield scrapy.Request(response.url, callback=self.parse_flat, dont_filter=True)

        

