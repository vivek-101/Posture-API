import bs4, requests
import random

url = 'https://www.yogajournal.com/poses/yoga-by-benefit/'

res = requests.get(url)
extensions = []
soup = bs4.BeautifulSoup(res.text, 'lxml')
body = soup.body
cards = body.findAll('a', {'class': 'm-card--image-link'})
for card in cards:
    ext = card['href']
    extensions.append(ext)

available_url = [ele.split('/')[-1] for ele in extensions]

def benefits(new_url):
    res = requests.get(new_url)
    ben = bs4.BeautifulSoup(res.text, 'lxml')
    page = ben.body.findAll('div', {'class', 'm-detail--body'})
    ul = page[0].find_all('ul')[-1]
    return [i.text for i in ul]
    # return ul


def exercise(name='anxiety', url='https://www.yogajournal.com/poses/yoga-by-benefit/'):
    target_url = url + name
    hit = requests.get(target_url)
    if hit.status_code == 200:
        page = bs4.BeautifulSoup(hit.text, 'lxml')
        page_exc = page.body.findAll('a', {'class': 'm-card--image-link'})
        exc_dict = dict()
        # try:
        for i in range(0, 12):
            try:
                images = page_exc[i].find('picture', {'class': 'is-waiting-to-load'})
                benefit = benefits('https://www.yogajournal.com'+page_exc[i]['href'])
                exc_dict[page_exc[i]['title']] = (images.source['data-srcset'].split(',')[-1].split(' ')[1],benefit)
            except Exception as e:
                pass
        val = random.sample(list(exc_dict), 3)
        return dict(zip(val, [exc_dict[x] for x in val]))
        # except ValueError as e:
        #     pass
    else:
        return 'Bad Request'
