from scrapy import Spider, Request
from yeastract_locus.items import YeastractLocusItem
import pandas as pd

url_stub = "http://www.yeastract.com/view.php?existing=locus&orfname="

class Yeastract_Spider(Spider):
    name = "yeastract_locus"
    allowed_urls = ["http://www.yeastract.com"]

    df_genes = pd.read_csv("labels_BP.csv", usecols = ["gene"])
    all_genes = df_genes["gene"].tolist()

    start_urls = [url_stub + i for i in all_genes]


    def parse(self, response):

        stdname = response.xpath('//td[@property="yontology:standardName_"]/text()').extract_first()
        sysname = response.xpath('//td[@property="yontology:systematicName_"]/text()').extract_first()

        print(stdname)
        print("="*55)
        print(sysname)
        print("="*55)

        item = YeastractLocusItem()
        item["stdname"] = stdname
        item["sysname"] = sysname

        yield item
