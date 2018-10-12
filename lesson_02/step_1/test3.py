'''
Using `<h1>`, enter card text contents, after the image 
    ```html
    <h1>Happy Birthday. Hope you are having a great day Michelle.</h1> 
    ```
'''

from bs4 import BeautifulSoup

with open('index3.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    
    for i in soup.find_all('body'):
        if i.find_all('div', attrs={'class':'birthday-card'}):
            assert(i.find('h1') and i.find('h1').get_text() == "Happy Birthday. Hope you are having a great day Michelle.")