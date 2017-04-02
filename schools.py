import re
import sys
import urllib.request

with urllib.request.urlopen('https://if.isuo.org/authorities/schools-list/id/620') as response:
    html = response.read()

result = ['', '', '']

header = 'School name, Phone, E-mail\n'

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
isuo = 'https://if.isuo.org/schools/view/id/'

nam, tel, email = '', '', ''
for school in re.finditer(r'(\<a href="/schools/view/id/)(.*?)("\>)', html.decode("utf-8")):
    id = school.group(2)
    url = isuo + id

    with urllib.request.urlopen(url) as resp:
        page = resp.read()

    for s_name in re.finditer(r'(\<h3\>)(.*?)(\<\/h3\>)', page.decode("utf-8"), flags=re.DOTALL):
        nam = s_name.group(2)
    for s_tel in re.finditer(r'(Телефони:\<\/th\>(.*?)\<td\>)(.*?)(\<\/td\>)', page.decode("utf-8"),
                             flags=re.DOTALL):  # findilng lazy backward from e-mail
        tel = s_tel.group(3)
    for s_email in re.finditer(r'(unescape\()(.*?)(\)\)\.remove)', page.decode("utf-8"), flags=re.DOTALL):
        email = urllib.request.unquote(s_email.group(2))
        for x in re.finditer(r'(\<a href="mailto:)(.*?)("\>)', email, flags=re.DOTALL):
            em = x.group(2)

    nam = '"' + nam.lstrip() + '"'
    tel = ',"' + tel + '"'
    em = ',"' + em + '"'
    print(nam.lstrip())
    print(tel)
    print(em)

    res_out = nam + tel + em  # showing only needed fields

    try:
        with open(filename, 'a') as csv:
            csv.write(res_out + '\n')
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
csv.close()
