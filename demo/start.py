from scrapy import cmdline

cmdline.execute("scrapy crawl baidu".split())

#保存为csv,json
# cmdline.execute("scrapy crawl baidu -o demo.csv".split())