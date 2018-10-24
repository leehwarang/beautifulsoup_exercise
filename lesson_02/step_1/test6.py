from bs4 import BeautifulSoup

with open('index6.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    pre_tag = soup.body.find('h6', class_="source-link")
    tag = pre_tag.find_next('a', href="https://www.freepik.com/free-photos-vectors/background")

    assert(
        tag
        and tag.find_parent('h6')
        and tag.text.strip() == 'Background vector created by Freepik'
    )

'''
1. Inside `<h6>` add`<a>` and after applying `href="https://www.freepik.com/free-photos-vectors/background"`to it, add the content below 
    ```html
    <h6 class="sources-link">
      <a href="https://www.freepik.com/free-photos-vectors/background">Background vector created by Freepik</a>
    </h6> 
    ```
'''
# from bs4 import BeautifulSoup

# with open('index6.html', 'r') as file:
#     soup = BeautifulSoup(file.read(), 'html.parser')

#     for i in soup.find_all('body'):
#         if i.find_all('h6', attrs={'class':'source-link'}):
#             assert(i.find('a', attrs={'href':'https://www.freepik.com/free-photos-vectors/background'}) and i.find('a').get_text() == "Background vector created by Freepik")
         