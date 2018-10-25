from bs4 import BeautifulSoup

with open('index6.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    try:
        pre_tag = soup.body.find('h2')
        tag = pre_tag.find_next('p')
    except AttributeError:
        assert()
    assert(
        pre_tag.text.strip() == '1. Introduction'
        and tag #p태그는 내용이 길어서 text 검사 안함
        and tag.find_parent('div')
    )

'''
#components of container - 1

from bs4 import BeautifulSoup

with open('index5.html', 'r') as file:
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

with open('index5.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    
    for i in soup.find_all('body'):
        if i.find('div', attrs={'class':'container'}):
            if i.find('h1') and i.find('h1').get_text() == "Google Play Terms of Service":
                print("성공")                
        else:
            print("실패")

#components of container - 3

from bs4 import BeautifulSoup

with open('index5.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    
    for i in soup.find_all('body'):
        if i.find('div', attrs={'class':'container'}):
            if i.find('h6') and i.find('h6').get_text() == "February 5, 2018":
                print("성공")                
        else:
            print("실패")

#components of container - 4

from bs4 import BeautifulSoup

with open('index5.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    
    for i in soup.find_all('body'):
        if i.find('div', attrs={'class':'container'}):
            if i.find('h2') and i.find('h2').get_text() == "1. Introduction":
                print("성공")                
        else:
            print("실패")
'''

# #components of container - 5

# from bs4 import BeautifulSoup

# with open('index5.html', 'r') as file:
#     soup = BeautifulSoup(file.read(), 'html.parser')
    
#     for i in soup.find_all('body'):
#         if i.find('div', attrs={'class':'container'}):
#             assert(i.find('p') and i.find('p').get_text() == '''Applicable Terms. Thanks for using Google Play. Google Play is a service provided by Google LLC ("Google", "we" or "us"), located at 1600 Amphitheatre Parkway, Mountain View, California 94043, USA. Your use of Google Play and the apps (including Android Instant Apps), games, music, movies, books, magazines, or other digital content or services (referred to as "Content") available through it is subject to these Google Play Terms of Service and the Google Terms of Service ("Google ToS") ( together referred to as the "Terms"). Google Play is a "Service" as described in the Google ToS. If there is any conflict between the Google Play Terms of Service and the Google ToS, the Google Play Terms of Service shall prevail.''')