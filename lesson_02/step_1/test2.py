from bs4 import BeautifulSoup

with open('index2.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    tag = soup.body.find('div', class_="birthday-card").find_next('img', src="https://image.freepik.com/free-vector/birthday-background-with-hand-drawn-gift_23-2147645419.jpg")

    assert(
        tag
        and tag.find_parent('div')
    )

# Add `<img>`, and apply `src="https://image.freepik.com/free-vector/birthday-background-with-hand-drawn-gift_23-2147645419.jpg"` and `alt="Birthday image"`. 
#     ```html
#     <img src="https://image.freepik.com/free-vector/birthday-background-with-hand-drawn-gift_23-2147645419.jpg" alt="Birthday Image">
#     ```

# from bs4 import BeautifulSoup

# with open('index2.html', 'r') as file:
#     soup = BeautifulSoup(file.read(), 'html.parser')
    
#     for i in soup.find_all('body'):
#         if i.find_all('div', attrs={'class':'birthday-card'}):
#             assert(i.find('img', attrs={'src':'https://image.freepik.com/free-vector/birthday-background-with-hand-drawn-gift_23-2147645419.jpg', 'alt':"Birthday Image"}))
         