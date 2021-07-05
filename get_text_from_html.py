import lxml.html
import sys
import newspaper
import os
f = sys.argv[1]
fw = open(os.path.join("download/html-txt", os.path.basename(f)), 'w')
html = lxml.html.parse(f)
texts = html.xpath("//div[contains(@class, 'l-contentMain')]/dl[contains(@class, 'listInterview')]//text()")
if len(texts) == 0:
  texts = html.xpath("//div[contains(@class, 'l-contentMain')]/div[contains(@class, 'm-grid')]//text()")
if len(texts) == 0:
  with open(f, 'rb') as fh:
    ht = fh.read()
  article = newspaper.Article(url=' ')
  article.set_html(ht)
  article.parse()
  fw.write(article.text)
  #  texts = html.xpath("//h4[contains(text(), '議事')]/following-sibling::*//text()")
fw.write('\n'.join(texts))
fw.write('\n')
