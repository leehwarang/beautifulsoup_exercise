'''
Add `<h2>` and apply `class="name"`.
```html
    <h2 class="name">Jonathan Harris</h2> 
'''

from bs4 import BeautifulSoup

with open('index3.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')

    for i in soup.find_all('body'):
        if i.find_all('div', attrs={'class':'business-card'}):
            assert(i.find('h2', attrs={'class':'name'}) and i.find('h2').get_text() == "Jonathan Harris")