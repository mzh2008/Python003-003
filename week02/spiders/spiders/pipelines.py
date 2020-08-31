# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

dbInfo = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'root',
    'password' : 'root',
    'db' : 'work1'
}
result = []

class ConnDB(object):
    def __init__(self, dbInfo, sqls):
        self.host = dbInfo['host']
        self.port = dbInfo['port']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db = dbInfo['db']
        self.sqls = sqls

    def run(self):
        conn = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            db = self.db
        )
        # 游标建立的时候就开启了一个隐形的事物
        cur = conn.cursor()
        try:
            for command in self.sqls:
                print(command)
                cur.execute(command)
                result.append(cur.fetchall())
            # 关闭游标
            cur.close()
            conn.commit()
        except:
            conn.rollback()
        # 关闭数据库连接
        conn.close()


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
        sql = "INSERT INTO maoyan_movie (m_name, m_type, m_date) VALUES ("'"+ name+ "','" + type+"','"+ date+"'");"
        print(sql)
        db = ConnDB(dbInfo, [sql])
        db.run()
        return item