# #components of container - 1

from bs4 import BeautifulSoup

with open('index2.html', 'r') as file:
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

with open('index2.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    
    for i in soup.find_all('body'):
        if i.find('div', attrs={'class':'container'}):
            if i.find('h1') and i.find('h1').get_text() == "Google Play Terms of Service":
                print("성공")                
        else:
            print("실패")


