import re
import urllib.request

with urllib.request.urlopen('http://www.codeabbey.com/index/user_ranking') as response:
    html = response.read()

i = 0
for td in re.finditer(r"<tr></tr>", html.decode("utf-8")):
    i += 1
    print(i, ' ', td)

print(html)
