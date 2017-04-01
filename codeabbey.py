import re
import urllib.request

with urllib.request.urlopen('http://www.codeabbey.com/index/user_ranking') as response:
    html = response.read()

rows = ['    Num', '    Lang', '    Rank', '    Enli', '    Shit', '    Tasks', 'Errr']
st = ''
i = 0
for tr in re.finditer(r'(\<tr class="centered none"\>)(.*?)(\<\/tr\>)', html.decode("utf-8"), flags=re.DOTALL):
    i += 1
    r = tr.group(2)
    #print('Row:', i)
    td_it = 0
    st = ''
    for td in re.finditer(r'(\<td\>)(.*?)(\<\/td\>)', r):
        d = td.group(2)
        #print(td_it, rows[td_it], d)

        if td_it == 2:
            for span in re.finditer(r'(\<span class="rank rank(.*?)\>)(.*?)(\<\/span\>)', r):
                #print('Eeee>', span.group(3))
                d = span.group(3)
        st = st + ',' + d
        td_it += 1

                #break
                # rows.append(r)
                # print(rows)
                # print (i, ' -> ',tr.group(0))
    st = st +'\n'
    #print (st[1:])
    with open('C:\\Users\\xxWolf\\Desktop\\SoftGroup\\Week7\\test1.csv', 'a') as csv:
        csv.write(st[1:])



csv.close()