# from bs4 import BeautifulSoup

# with open('index7.html', 'r') as file:
#     soup = BeautifulSoup(file.read(), 'html.parser')
#     h2_list = []
#     for i in soup.find_all('body'):
#         if i.find('div', attrs={'class':'container'}):
#             h2_list = i.find_all('h2')
#     assert(h2_list[2].get_text() == "3. Purchases and Payments")




from bs4 import BeautifulSoup

with open('index7.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    p_list = []
    for i in soup.find_all('body'):
        if i.find('div', attrs={'class':'container'}):
            p_list = i.find_all('p')
    assert(p_list[2].get_text() == """Content on Google Play is offered by Google Commerce Limited, and when you download, view, use or purchase Content on or using Google Play, you will enter into a separate contract based on these Terms (as applicable) with Google Commerce Limited.""") 
