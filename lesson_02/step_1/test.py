from bs4 import BeautifulSoup

with open('index.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    tag = soup.body.find('div', class_="birthday-card")

    assert(
        tag
        and tag.find_parent('body')
    )

#Add `<div>` within `<body>` and apply `class="birthday-card`.

# from bs4 import BeautifulSoup

# with open('index.html', 'r') as file:
#     soup = BeautifulSoup(file.read(), 'html.parser')
    
#     for i in soup.find_all('body'):
#         assert(i.find_all('div', attrs={'class':'birthday-card'}))