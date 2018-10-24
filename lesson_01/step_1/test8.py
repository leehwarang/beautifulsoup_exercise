from bs4 import BeautifulSoup

with open('index8.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    first_tag = soup.body.find_all('h2')
    second_tag = soup.body.find_all('p')

    assert(
        len(first_tag) == 3
        and len(second_tag) == 3 #p태그는 내용이 길어서 text 검사 안함
        and first_tag[2].text.strip() == '3. Purchases and Payments'
        and first_tag[2].previous_sibling.previous_sibling.name == 'p'
        and second_tag[2].previous_sibling.previous_sibling.name == 'h2'
        and first_tag[2].find_parent('div')
        and second_tag[2].find_parent('div')
    )

# from bs4 import BeautifulSoup

# with open('index7.html', 'r') as file:
#     soup = BeautifulSoup(file.read(), 'html.parser')
#     h2_list = []
#     for i in soup.find_all('body'):
#         if i.find('div', attrs={'class':'container'}):
#             h2_list = i.find_all('h2')
#     assert(h2_list[2].get_text() == "3. Purchases and Payments")




# from bs4 import BeautifulSoup

# with open('index7.html', 'r') as file:
#     soup = BeautifulSoup(file.read(), 'html.parser')
#     p_list = []
#     for i in soup.find_all('body'):
#         if i.find('div', attrs={'class':'container'}):
#             p_list = i.find_all('p')
#     assert(p_list[2].get_text() == """Content on Google Play is offered by Google Commerce Limited, and when you download, view, use or purchase Content on or using Google Play, you will enter into a separate contract based on these Terms (as applicable) with Google Commerce Limited.""") 
