import scrapy
import pandas as pd
app_packages_data_df = pd.read_csv('top_app_package.csv')
# # print(app_packages_data_df)

class AppDetailScrapper(scrapy.Spider):
    name = 'app_detailer'


    # allowed_domains = ['www.play.google.com/store/apps/details?id=nic.goi.aarogyasetu']
    start_urls = set(app_packages_data_df["app_url"].values[0:10])
    print(start_urls)


    # def link_parser(self, response):
    #     links = [link for link in app_packages_data_df['app_url']]
    #     for link in links:
    #         yield scrapy.Request(url=link, callback=self.parse)
    #
    #
    try:
        def parse(self, response):
            # intro_block = response.xpath('//div[contains(@class,"JNury")]//div[@class="rlnrKc"]')
            print(response.request.url.split('=')[-1])
            #
            # app_name = response.xpath('//*[@itemprop="name"]/span/text()').extract_first()  # check extract_first()
            # genre = response.xpath('//*[@itemprop="genre"]/text()').extract()
            # app_url = response.xpath('//*[@itemprop="url"]/@content').extract_first()
            # price = response.xpath('//*[@itemprop="price"]/@content').extract_first()
            # description = response.xpath('//*[@itemprop="description"]/span/div/text()').extract()
            #
            # # print()
            # # print()
            # # print("*"*80)
            # # print()
            # # print((
            # #     app_name, genre, app_url, price, description
            # #     ))
            # # print()
            # # print("*"*80)
            # # print()
            # # print()
            #
            # yield app_name
    except:
        print('*'*80, "PARSING ERROR")
