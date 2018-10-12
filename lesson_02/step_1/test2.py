# Add `<img>`, and apply `src="https://image.freepik.com/free-vector/birthday-background-with-hand-drawn-gift_23-2147645419.jpg"` and `alt="Birthday image"`. 
#     ```html
#     <img src="https://image.freepik.com/free-vector/birthday-background-with-hand-drawn-gift_23-2147645419.jpg" alt="Birthday Image">
#     ```

from bs4 import BeautifulSoup

with open('index2.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    
    for i in soup.find_all('body'):
        if i.find_all('div', attrs={'class':'birthday-card'}):
            assert(i.find('img', attrs={'src':'https://image.freepik.com/free-vector/birthday-background-with-hand-drawn-gift_23-2147645419.jpg', 'alt':"Birthday Image"}))
         