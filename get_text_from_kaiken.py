import lxml.html
import sys
html = lxml.html.parse(sys.argv[1])
print("<doc>")
nodes = html.xpath('//dl[contains(@class, "Interview")]/*')
for node in nodes:
    t = node.xpath('./self::dt/text()')
    if len(t) > 0:
        print("<turn>", end=' ')
        print(t[0][:-1], end=' ')
    t = node.xpath('./self::dd/text()')
    if len(t) > 0:
        print(t[0])
