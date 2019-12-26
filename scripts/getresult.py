import requests
import bs4 

res = requests.Session().get('https://leetcode.com/xiuxiu_/')
soup = bs4.BeautifulSoup(res.text, 'lxml')
submissions = soup.findAll('a', href=lambda h: h and h.startswith("/problems"))
for s in submissions[:4]:
    t = s.text.split('\n')
    print('\t'.join([l.replace("\n", "").strip().lstrip() for l in t if l]))
    # for line in t:
        # print(line.lstrip().strip())
