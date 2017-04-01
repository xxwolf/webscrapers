import re
import sys
import urllib.request

with urllib.request.urlopen('http://www.codeabbey.com/index/user_ranking') as response:
    html = response.read()

st = ''
result = ['', '', '', '', '', '']

header = 'Number, Username, Rank, Enlightenment, Tasks solved\n'

if len(sys.argv) < 2:
    print('Need file name')
    sys.exit()
else:
    filename = sys.argv[1]

try:
    with open(filename, 'a') as csv:
        csv.write(header)

except IOError as e:
    print("I/O error({0}): {1}".format(e.errno, e.strerror))
csv.close()

i = 0
for tr in re.finditer(r'(\<tr class="centered none"\>)(.*?)(\<\/tr\>)', html.decode("utf-8"), flags=re.DOTALL):
    i += 1
    r = tr.group(2)
    td_it = 0
    for td in re.finditer(r'(\<td\>)(.*?)(\<\/td\>)', r):
        d = td.group(2)
        result[td_it] = d

        if td_it == 1:
            for user in re.finditer(r'(\<a href=(.*?)\>)(.*?)(\<\/a\>)', r):
                u = user.group(3)
                result[1] = u

        if td_it == 2:
            for span in re.finditer(r'(\<span class="rank rank(.*?)\>)(.*?)(\<\/span\>)', r):
                d = u + span.group(3)
                result[2] = span.group(3)

        td_it += 1

    res_out = result[0:4] + result[5:6]  # showing only needed fields
    r_o = ''
    for smt in res_out:
        r_o = r_o + ',' + '"' + smt + '"'
    try:
        with open(filename, 'a') as csv:
            csv.write(r_o[1:] + '\n')
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
csv.close()