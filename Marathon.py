import re

text = '   gf  gfdAAA1234ZZZuijjk'
x = re.search("[^\s]+", text)

print(x.group())