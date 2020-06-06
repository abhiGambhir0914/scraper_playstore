import scrapy
from scrapy_splash import SplashRequest

script = """
        function main(splash)
            local num_scrolls = 1000
            local scroll_delay = 200

            local scroll_to = splash:jsfunc("window.scrollTo")
            local get_body_height = splash:jsfunc(
                "function() {return document.body.scrollHeight;}"
            )
            assert(splash:go(splash.args.url))
            

            for _ = 1, num_scrolls do
                local height = get_body_height()
                for i = 1, num_scrolls do
                    scroll_to(0, height * i/10)
                    splash:wait(20)
                end
            end  
                  
            return splash:html()
        end
        """

test_script = """
function main(splash)
    assert(splash:go(splash.args.url))
  
    local scroll_to = splash:jsfunc("window.scrollTo")
    scroll_to(0, 100000)
    splash:wait(20)

    return {html=splash:html(),png=splash:png()}
end 
"""

another_script = """
    function main(splash)
        local num_scrolls = 10
        local scroll_delay = 10
        local scroll_to = splash:jsfunc("window.scrollTo")
        local get_body_height = splash:jsfunc(
            "function() {return document.body.scrollHeight;}"
        )
        assert(splash:go(splash.args.url))
        splash:wait(splash.args.wait)

        for _ = 1, num_scrolls do
            scroll_to(0, get_body_height())
            splash:wait(scroll_delay)
        end        
       
    end
    """

class AppDetailScrapper(scrapy.Spider):
    name = 'app_detailer'

    # allowed_domains = ['www.play.google.com/store/apps/details?id=nic.goi.aarogyasetu']
    start_urls = ['https://play.google.com/store/apps/collection/cluster?clp=0g4jCiEKG3RvcHNlbGxpbmdfZnJlZV9BUFBMSUNBVElPThAHGAM%3D:S:ANO1ljKs-KA&gsr=CibSDiMKIQobdG9wc2VsbGluZ19mcmVlX0FQUExJQ0FUSU9OEAcYAw%3D%3D:S:ANO1ljL40zU']


    def start_requests(self):
        

        # for url in response.xpath(xp).extract():
        #     print(url)

        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                endpoint='execute',
                args={
                    'lua_source': test_script, 
                    'wait': 2, 
                    'timeout' : 90,
                   },
                # cache_args=['lua_source'] 
                # 'slot_policy': scrapy_splash.SlotPolicy.PER_DOMAIN,
            )


    def parse(self, response):
        # print("Here...........")
        count = 0
        xp = '//div[contains(@class,"vU6FJ")]/a/@href'
        
        for url in response.xpath(xp).extract():
            count = count + 1
            print(url)
        print(count)
        
    

    # def parse(self, response):
    #     # intro_block = response.xpath('//div[contains(@class,"JNury")]//div[@class="rlnrKc"]')

    #     app_name = response.xpath('//*[@itemprop="name"]/span/text()').extract_first()  # check extract_first()
    #     genre = response.xpath('//*[@itemprop="genre"]/text()').extract()
    #     app_url = response.xpath('//*[@itemprop="url"]/@content').extract_first()
    #     price = response.xpath('//*[@itemprop="price"]/@content').extract_first()
    #     description = response.xpath('//*[@itemprop="description"]/span/div/text()').extract()

    #     print()
    #     print()
    #     print("*"*80)
    #     print()
    #     print((
    #         app_name, genre, app_url, price, description
    #         ))
    #     print()
    #     print("*"*80)
    #     print()
    #     print()




    #     # company_name = 
    #     # downloads = 
    #     # contains_ads =


       
    #     # //div[contains(@class,"JNury")]/div[@class="rlnrKc"]

    # #    //div[contains(@class,"_1oQyIsiPHYt6nx7VOmd1sz")]//div[contains(@class,"_2FCtq-QzlfuN-SwVMUZMM3")]
       
    #     # for item in response.xpath('//div[contains(@class,"W4P4ne ")]').extract():
    #     #     #create a dictionary to store the scraped info
    #     #     print('*'*20,item)

    #     #     #yield or give the scraped info to scrapy
    #     yield app_name
    