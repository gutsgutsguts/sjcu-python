import requests
from bs4 import BeautifulSoup

res = requests.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EC%BD%94%EC%98%A4%EB%A1%B1+%EA%B8%B0%EB%8A%A5%EC%84%B1+%EB%B0%98%ED%8C%94&oquery=%EC%BD%94%EB%A1%B1+%EA%B8%B0%EB%8A%A5%EC%84%B1+%EB%B0%98%ED%8C%94&tqi=iC7m4wpzL8VsskIv7DGssssss4l-491415')
print(res.content)

soup = BeautifulSoup(res.content, 'html.parser')

title = soup.find('title')
print(title.get_text())

total_tit = soup.find_all( class_ = 'totla_tit')
for one in total_tit:
    print(one.getText())
    