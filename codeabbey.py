import re
import urllib.request

with urllib.request.urlopen('http://www.codeabbey.com/index/user_ranking') as response:
    html = response.read()

rows = ['    Num', '    Lang', '    Rank', '    Enli', '    Shit', '    Tasks', 'Errr']

i = 0
for tr in re.finditer(r'(\<tr class="centered none"\>)(.*?)(\<\/tr\>)', html.decode("utf-8"), flags=re.DOTALL):
    i += 1
    r = tr.group(2)
    print('Row:', i)
    td_it = 0
    for td in re.finditer(r'(\<td\>)(.*?)(\<\/td\>)', r):

        d = td.group(2)

        print(td_it, rows[td_it], d)
        td_it += 1
        if td_it == 2:
            for span in re.finditer(r'(\<span class="rank rank(.*?)\>)(.*?)(\<\/span\>)', r):
                print('Eeee>', span.group(3))
                continue
                # rows.append(r)
                # print(rows)
                # print (i, ' -> ',tr.group(0))
