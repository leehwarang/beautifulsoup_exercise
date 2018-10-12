'''
1. Below `<div class="birthday-card">` add `<h6>` and apply `class="sources-link"` to it.
    ```html
    <h6 class="sources-link"></h6>
    ```
'''


from bs4 import BeautifulSoup

with open('index5.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    
    for i in soup.find_all('body'):
        assert(i.find('h6', attrs={'class':'source-link'}))
         