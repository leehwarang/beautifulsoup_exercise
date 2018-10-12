'''
    ```
1. After the contents, use `<h3>` to enter the card author 
    ```html
    <h3>from Frank</h3>
    ```
'''
from bs4 import BeautifulSoup

with open('index4.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    
    for i in soup.find_all('body'):
        if i.find('div', attrs={'class':'birthday-card'}):
            assert(i.find('h3') and i.find('h3').get_text() == "from Frank")
  