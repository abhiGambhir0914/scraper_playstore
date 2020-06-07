import scrapy
import pandas as pd
from ..items import PlaystorescrapyItem

app_packages_data_df = pd.read_csv('top_app_package.csv')
# # print(app_packages_data_df)

class AppDetailScrapper(scrapy.Spider):
    name = 'app_detailer'



    # allowed_domains = ['www.play.google.com/store/apps/details?id=nic.goi.aarogyasetu']
    start_urls = set(app_packages_data_df["app_url"].values)
    # print(start_urls)

    custom_settings = {
        'FEED_URI': 'top_apps_details.csv',
        'FEED_FORMAT': 'csv',
        'FEED_EXPORTERS': {
            'csv': 'scrapy.exporters.CsvItemExporter',
        },
        'FEED_EXPORT_ENCODING': 'utf-8',
    }


    # def link_parser(self, response):
    #     links = [link for link in app_packages_data_df['app_url']]
    #     for link in links:
    #         yield scrapy.Request(url=link, callback=self.parse)
    #

    try:
        def parse(self, response):
            items = PlaystorescrapyItem()
            # intro_block = response.xpath('//div[contains(@class,"JNury")]//div[@class="rlnrKc"]')
            # print(response.request.url.split('=')[-1])
            #

            # ================================ ON HOLD ===========================================
            # app_url = response.xpath('//*[@itemprop="url"]/@content').extract_first()
            #
            #
            #
            # =============================================================================

            section_app_header = response.xpath('//div[contains(@class,"JNury")]/div[1]//div[contains(@class,"oQ6oV")]')
            section_reviews_numbers = response.xpath('//div[contains(@class,"W4P4ne")]//div[@class="K9wGie"]')
            section_additional_info = response.xpath('//div[contains(@class,"JNury")]//div[contains(@class,"W4P4ne")]')
            # section_app_reviews = response.xpath('//div[contains(@class,"JNury")]//div[contains(@class,"W4P4ne")]').extract()



            app_package_name = response.request.url.split('=')[-1]
            app_image_url = section_app_header.xpath('.//div[@class="xSyT2c"]/img/@src').extract_first()
            app_name = response.xpath('//*[@itemprop="name"]/span/text()').extract_first()  # check extract_first()
            genre = response.xpath('//*[@itemprop="genre"]/text()').extract()
            price = response.xpath('//*[@itemprop="price"]/@content').extract_first()

            try:
                if int(price) == 0:
                    price_type = 'Free'
                elif int(price) > 0:
                    price_type = 'Paid'
            except:
                print("Error Parsing Price_Type")

            author = response.xpath('.//div[@class="jdjqLd"]/div[1]//span[1]/a/text()').extract_first()
            author_play_store_company_url = 'https://play.google.com' + str(section_app_header.xpath('.//div[@class="jdjqLd"]/div[1]//span[1]/a/@href').extract_first())
            rating_value = section_reviews_numbers.xpath('./div[contains(@aria-label, "stars")]/text()').extract_first()
            review_number = section_reviews_numbers.xpath('./span/span[contains(@aria-label, "rating")]/text()').extract_first()

            updated = section_additional_info.xpath('.//div[contains(text(),"Updated")]/..//div/span[@class="htlgb"]/text()').extract_first()
            app_size = section_additional_info.xpath('.//div[contains(text(),"Size")]/..//div/span[@class="htlgb"]/text()').extract_first()
            downloads = section_additional_info.xpath('.//div[contains(text(),"Installs")]/..//div/span[@class="htlgb"]/text()').extract_first()
            current_version = section_additional_info.xpath('.//div[contains(text(),"Version")]/..//div/span[@class="htlgb"]/text()').extract_first()
            compatibility = section_additional_info.xpath('.//div[contains(text(),"Android")]/..//div/span[@class="htlgb"]/text()').extract_first()
            content_rating = section_additional_info.xpath('.//div[contains(text(),"Content")]/..//div/span[@class="htlgb"]/div/text()').extract_first()
            in_app_products = section_additional_info.xpath('.//div[contains(text(),"In-app")]/..//div/span[@class="htlgb"]/text()').extract_first()
            developer_website = section_additional_info.xpath('.//div[contains(text(),"Developer")]/..//div/span[@class="htlgb"]//div/a[contains(text(),"website")]/@href').extract_first()
            developer_email = section_additional_info.xpath('.//div[contains(text(),"Developer")]/..//div/span[@class="htlgb"]//div/a[contains(@href,"mailto:")]/text()').extract_first()
            developer_address = response.xpath('normalize-space(string(//div[contains(@class,"JNury")]//div[contains(@class,"W4P4ne")]//div[contains(text(),"Developer")]/..//div/span[@class="htlgb"]//div[not(*)]/text()))').extract_first()
            description = response.xpath('normalize-space(string(//*[@itemprop="description"]/span/div))').extract_first()

            items['app_package_name'] = app_package_name
            items['app_image_url'] = app_image_url
            items['app_name'] = app_name
            items['genre'] = genre
            items['price'] = price
            items['price_type'] = price_type
            items['author'] = author
            items['author_play_store_company_url'] = author_play_store_company_url
            items['rating_value'] = rating_value
            items['review_number'] = review_number
            items['updated'] = updated
            items['app_size'] = app_size
            items['downloads'] = downloads
            items['current_version'] = current_version
            items['compatibility'] = compatibility
            items['content_rating'] = content_rating
            items['in_app_products'] = in_app_products
            items['developer_website'] = developer_website
            items['developer_email'] = developer_email
            items['developer_address'] = developer_address
            items['description'] = description

            yield items


    except:
        print('*'*80, "PARSING ERROR")
        raise CloseSpider('subdomain limit reached')





