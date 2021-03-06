from bs4 import BeautifulSoup

with open('index5.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    try:
        pre_tag = soup.body.find('h6')
        tag = pre_tag.find_next('h2')
    except AttributeError:
        assert()
    assert(
        pre_tag.text.strip() == 'February 5, 2018'
        and tag
        and tag.text.strip() =='1. Introduction'
        and tag.find_parent('div')
    )

'''
#components of container - 1

from bs4 import BeautifulSoup

with open('index4.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    
    for i in soup.find_all('body'):
        if i.find('div', attrs={'class':'container'}):
            if i.find('img', attrs={'src':'img_google_play.png', 'alt':'Google Play'}):
                if i.find('h1')
                print("성공")
        else:
            print("실패")

#components of container - 2

from bs4 import BeautifulSoup

with open('index4.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    
    for i in soup.find_all('body'):
        if i.find('div', attrs={'class':'container'}):
            if i.find('h1') and i.find('h1').get_text() == "Google Play Terms of Service":
                print("성공")                
        else:
            print("실패")

#components of container - 3

from bs4 import BeautifulSoup

with open('index4.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    
    for i in soup.find_all('body'):
        if i.find('div', attrs={'class':'container'}):
            if i.find('h6') and i.find('h6').get_text() == "February 5, 2018":
                print("성공")                
        else:
            print("실패")
'''
'''
#components of container - 4

from bs4 import BeautifulSoup

with open('index4.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    
    for i in soup.find_all('body'):
        if i.find('div', attrs={'class':'container'}):
            assert(i.find('h2') and i.find('h2').get_text() == "1. Introduction")
'''