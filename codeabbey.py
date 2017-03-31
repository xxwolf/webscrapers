import re
import urllib.request

with urllib.request.urlopen('http://www.codeabbey.com/index/user_ranking') as response:
    html = response.read()
# r'((\<tr class="centered none"\>).*?(\<\/tr\>))'

# m = re.match(r'(?P<start>\<tr class="centered none"\>)(?P<inner>.*?)(?P<finish>\<\/tr\>)', html.decode("utf-8"), )
# print (m)

rows = []
i = 0
for tr in re.finditer(r'\<tr class="centered none"\>.*?(\<\/tr\>)', html.decode("utf-8"), flags=re.DOTALL):
    i += 1
    # print (i)
    r = tr.group(0)
    rows.append(r)
    print(rows)
    #print (i, ' -> ',tr.group(0))
