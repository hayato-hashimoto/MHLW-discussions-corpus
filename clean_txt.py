import os
import sys
import re

def process_line(l):
    if l == "":
      return
    if re.sub('[\-参ー\s　0-9０-９A-Za-z]', '', l) == '':
      return
    if l.startswith(" "):
      print()
    l = re.sub('^　*|　*$', '', l)
    if len(l) > 1500 and '○' in l:
      turns = l.split('○')
      if len(turns) > 2:
        for ll in turns:
          process_line('○' + ll)
        return
    if l.startswith("○"):
      if len(l) == 1: return
      name = l[1:].split()[0]
      print("\n<turn>", end=' ')
      print(name, end=' ')
      l = ' '.join(l[1:].split()[1:])
    # l = re.sub('([^a-zA-Z0-9]) +([^a-zA-Z0-9])', '\\1\\2', l)
    if l.startswith("【"):
      l = re.sub('【(.*?)】', "\\1", l)
    print(l, end="")
    if l.endswith("。"):
      print()

for filename in os.listdir(sys.argv[1]):
  print("<doc>")
  with open(os.path.join(sys.argv[1], filename)) as f:
    for l in f:
      l = l.strip()
      process_line(l)
print()
