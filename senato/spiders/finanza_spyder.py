# -*- coding: utf-8 -*-

import os
import re

import scrapy

AMENDMENT_XPATH = '//dl[@class="emendamenti"]/dt/a/@href'
AMENDMENT_URL = '/leg/19/BGT/Testi/Emend/0{parent}//0{_id}.akn'
HREF_REGEX = r'id=(?P<_id>\d+)&idoggetto=(?P<parent>\d+)'

class FinanzaSpider(scrapy.Spider):
    name = 'garante'
    allowed_domains = ['senato.it']
    start_urls = ['https://www.senato.it/leg/19/BGT/Schede/Ddliter/testi/56123_testi.htm']
                    
    def parse(self, response):
        for href in response.xpath(AMENDMENT_XPATH).extract():
            match = re.search(HREF_REGEX, href)
            if match:
                _id = match.group('_id')
                parent = match.group('parent')

                relative_url = AMENDMENT_URL.format(_id=_id, parent=parent)
                absolute_url = response.urljoin(relative_url)

                yield scrapy.Request(absolute_url, callback=self.download_amendment)

    def download_amendment(self, response):
        relative_filename = response.url.split('/')[-1]
        absolute_filename = os.path.join(os.getcwd(), 'data', self.name, relative_filename)

        with open(absolute_filename, 'wb') as f:
            f.write(response.body)
