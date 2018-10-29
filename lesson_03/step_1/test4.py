from bs4 import BeautifulSoup

with open('index4.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    try:
        tag = soup.body.find('h2', class_="name").find_next('ul', class_="information")
    except AttributeError:
        assert()
    assert(
        tag
        and tag.previous_sibling.previous_sibling.name == 'h2'
        and tag.find_parent('div')
    )

'''
Add `<ul>` and apply `class="information"`. 
    ```html
    <ul class="information"></ul>
    ```
'''


# from bs4 import BeautifulSoup

# with open('index4.html', 'r') as file:
#     soup = BeautifulSoup(file.read(), 'html.parser')

#     for i in soup.find_all('body'):
#         if i.find_all('div', attrs={'class':'business-card'}):
#             assert(i.find('ul', attrs={'class':'information'}))