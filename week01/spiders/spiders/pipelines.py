# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SpidersPipeline:
    def process_item(self, item, spider):
        name = item['name']
        type = item['type']
        date = item['date']
        import csv
        f = open('./maoyanmovie.csv','a+',encoding='utf-8', newline='')
        csv_writer = csv.writer(f)
        csv_writer.writerow([name, type, date])
        f.close()
        return item