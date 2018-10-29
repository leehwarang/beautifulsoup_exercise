from bs4 import BeautifulSoup

with open('index3.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    try:
        tag = soup.body.find('img', class_="image", src="https://cdn3.iconfinder.com/data/icons/fantasy-and-role-play-game-adventure-quest/512/Orc-512.png").find_next('h2', class_="name")
    except AttributeError:
        assert()
    assert(
        tag
        and tag.text.strip() =='Jonathan Harris'
        and tag.previous_sibling.previous_sibling.name == 'img'
        and tag.find_parent('div')
    )

'''
Add `<h2>` and apply `class="name"`.
```html
    <h2 class="name">Jonathan Harris</h2> 
'''

# from bs4 import BeautifulSoup

# with open('index3.html', 'r') as file:
#     soup = BeautifulSoup(file.read(), 'html.parser')

#     for i in soup.find_all('body'):
#         if i.find_all('div', attrs={'class':'business-card'}):
#             assert(i.find('h2', attrs={'class':'name'}) and i.find('h2').get_text() == "Jonathan Harris")