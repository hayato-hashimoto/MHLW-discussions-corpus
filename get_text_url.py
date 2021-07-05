import re
import lxml.html
import sys
filename = sys.argv[1]
html = lxml.html.parse(filename)
urls = html.xpath("//a[contains(text(), '議事録')]/@href")
for url in urls:
  print(url)
