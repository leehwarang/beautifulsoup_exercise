from bs4 import BeautifulSoup

with open('index4.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    pre_tag = soup.body.find('h1')
    tag = pre_tag.find_next('h6')

    
    assert(
        pre_tag.text.strip() == 'Google Play Terms of Service'
        and tag
        and tag.text.strip() =='February 5, 2018'
        and tag.find_parent('div')
    )

'''
#components of container - 1

from bs4 import BeautifulSoup

with open('index3.html', 'r') as file:
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

with open('index3.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    
    for i in soup.find_all('body'):
        if i.find('div', attrs={'class':'container'}):
            if i.find('h1') and i.find('h1').get_text() == "Google Play Terms of Service":
                print("성공")                
        else:
            print("실패")
'''
'''
#components of container - 3

from bs4 import BeautifulSoup

with open('index3.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    
    for i in soup.find_all('body'):
        if i.find('div', attrs={'class':'container'}):
            assert(i.find('h6') and i.find('h6').get_text() == "February 5, 2018")


#개선 할 점
#TC를 4개로 나누어야 함. 
#TC1: body에 div가 1개 있는지
#TC2: div에 img가 1개 있는지
#TC3: div에 img 밑에 h1이 1개 있는지
#TC4: h1 밑에 h6이 1개 있는지
'''