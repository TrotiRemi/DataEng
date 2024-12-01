import scrapy

class ChurchillQuotesSpider(scrapy.Spider):
    name = "citations_de_churchill"
    start_urls = ["http://evene.lefigaro.fr/citations/winston-churchill"]

    def parse(self, response):
        for cit in response.xpath('//div[@class="figsco__quote__text"]'):
            text_value = cit.xpath('a/text()').extract_first()

            # Retirer les caractères “ et ”
            if text_value:
                text_value = text_value.replace("“", "").replace("”", "")

            yield {'text': text_value}