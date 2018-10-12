'''
Add `<ul>` and apply `class="information"`. 
    ```html
    <ul class="information"></ul>
    ```
'''


from bs4 import BeautifulSoup

with open('index4.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')

    for i in soup.find_all('body'):
        if i.find_all('div', attrs={'class':'business-card'}):
            assert(i.find('ul', attrs={'class':'information'}))