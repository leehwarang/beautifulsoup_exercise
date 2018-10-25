from bs4 import BeautifulSoup

with open('index4.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    try:
        pre_tag = soup.body.find('h1')
        tag = pre_tag.find_next('h3')
    except AttributeError:
        assert()
    
    assert(
        pre_tag.text.strip() == 'Happy Birthday. Hope you are having a great day Michelle.'
        and tag
        and tag.text.strip() =='from Frank'
        and tag.previous_sibling.previous_sibling.name == 'h1'
        and tag.find_parent('div')
    )

'''
    ```
1. After the contents, use `<h3>` to enter the card author 
    ```html
    <h3>from Frank</h3>
    ```
'''
# from bs4 import BeautifulSoup

# with open('index4.html', 'r') as file:
#     soup = BeautifulSoup(file.read(), 'html.parser')
    
#     for i in soup.find_all('body'):
#         if i.find('div', attrs={'class':'birthday-card'}):
#             assert(i.find('h3') and i.find('h3').get_text() == "from Frank")
  