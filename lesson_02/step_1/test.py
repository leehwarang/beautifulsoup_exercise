#Add `<div>` within `<body>` and apply `class="birthday-card`.

from bs4 import BeautifulSoup

with open('index.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    
    for i in soup.find_all('body'):
        assert(i.find_all('div', attrs={'class':'birthday-card'}))