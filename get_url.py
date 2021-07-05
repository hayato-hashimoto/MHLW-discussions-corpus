import re
import lxml.html
import sys
filename = sys.argv[1]
html = lxml.html.parse(filename)
urls = html.xpath("//div[@class='l-contentMain']//li//a/@href")
for url in urls:
  print(url)
