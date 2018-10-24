from bs4 import BeautifulSoup

with open('index3.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    tag = soup.body.find('img', src="https://image.freepik.com/free-vector/birthday-background-with-hand-drawn-gift_23-2147645419.jpg").find_next('h1')
    
    assert(
        tag
        and tag.text.strip() =='Happy Birthday. Hope you are having a great day Michelle.'
        and tag.previous_sibling.previous_sibling.name == 'img'
        and tag.find_parent('div')
    )

#만약 find('img')를 찾지 못했다면, find_next()를 실행할 수 없음.
'''
Using `<h1>`, enter card text contents, after the image 
    ```html
    <h1>Happy Birthday. Hope you are having a great day Michelle.</h1> 
    ```
'''

# from bs4 import BeautifulSoup

# with open('index3.html', 'r') as file:
#     soup = BeautifulSoup(file.read(), 'html.parser')
    
#     for i in soup.find_all('body'):
#         if i.find_all('div', attrs={'class':'birthday-card'}):
#             assert(i.find('h1') and i.find('h1').get_text() == "Happy Birthday. Hope you are having a great day Michelle.")