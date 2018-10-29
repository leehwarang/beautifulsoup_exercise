from bs4 import BeautifulSoup

with open('index.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    tag = soup.body.find('div', class_="business-card")

    assert(
        tag
        and tag.find_parent('body')
    )

'''
1. Add `<div>` within `<body>` and apply `class="business-card"`.
'''

# from bs4 import BeautifulSoup

# with open('index.html', 'r') as file:
#     soup = BeautifulSoup(file.read(), 'html.parser')

#     for i in soup.find_all('body'):
#         assert(i.find_all('div', attrs={'class':'business-card'}))