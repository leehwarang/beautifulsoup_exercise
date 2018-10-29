from bs4 import BeautifulSoup

with open('index2.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    try:
        tag = soup.body.find('div', class_="business-card").find_next('img', class_="image", src="https://cdn3.iconfinder.com/data/icons/fantasy-and-role-play-game-adventure-quest/512/Orc-512.png")
    except AttributeError:
        assert()
    assert(
        tag
        and tag.find_parent('div')
    )

'''
Add `<img>` and apply `class="image"` and `alt="Profile image"`.

    ```html
    <img class="image" src="https://cdn3.iconfinder.com/data/icons/fantasy-and-role-play-game-adventure-quest/512/Orc-512.png" alt="Profile image">
'''

# from bs4 import BeautifulSoup

# with open('index2.html', 'r') as file:
#     soup = BeautifulSoup(file.read(), 'html.parser')

#     for i in soup.find_all('body'):
#         if i.find_all('div', attrs={'class':'business-card'}):
#             assert(i.find('img', attrs={'src':"https://cdn3.iconfinder.com/data/icons/fantasy-and-role-play-game-adventure-quest/512/Orc-512.png", 'alt':"Profile image"}))