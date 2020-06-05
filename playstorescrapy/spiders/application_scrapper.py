import scrapy

class AppDetailScrapper(scrapy.Spider):
    name = 'app_detailer'

    allowed_domains = ['www.play.google.com/store/apps/details?id=nic.goi.aarogyasetu']
    start_urls = ['https://play.google.com/store/apps/details?id=nic.goi.aarogyasetu']

    # asd

    def parse(self, response):
        # intro_block = response.xpath('//div[contains(@class,"JNury")]//div[@class="rlnrKc"]')

        app_name = response.xpath('//*[@itemprop="name"]/span/text()').extract_first()  # check extract_first()
        genre = response.xpath('//*[@itemprop="genre"]/text()').extract()
        app_url = response.xpath('//*[@itemprop="url"]/@content').extract_first()
        price = response.xpath('//*[@itemprop="price"]/@content').extract_first()
        description = response.xpath('//*[@itemprop="description"]/span/div/text()').extract()

        print()
        print()
        print("*"*80)
        print()
        print((
            app_name, genre, app_url, price, description
            ))
        print()
        print("*"*80)
        print()
        print()




        # company_name = 
        # downloads = 
        # contains_ads =


       
        # //div[contains(@class,"JNury")]/div[@class="rlnrKc"]

    #    //div[contains(@class,"_1oQyIsiPHYt6nx7VOmd1sz")]//div[contains(@class,"_2FCtq-QzlfuN-SwVMUZMM3")]
       
        # for item in response.xpath('//div[contains(@class,"W4P4ne ")]').extract():
        #     #create a dictionary to store the scraped info
        #     print('*'*20,item)

        #     #yield or give the scraped info to scrapy
        yield app_name
    