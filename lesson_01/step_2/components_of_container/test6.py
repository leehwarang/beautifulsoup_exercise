
# #components of container - 1

# from bs4 import BeautifulSoup

# with open('index6.html', 'r') as file:
#     soup = BeautifulSoup(file.read(), 'html.parser')
    
#     for i in soup.find_all('body'):
#         if i.find('div', attrs={'class':'container'}):
#             if i.find('img', attrs={'src':'img_google_play.png', 'alt':'Google Play'}):
#                 if i.find('h1')
#                 print("성공")
#         else:
#             print("실패")

# #components of container - 2

# from bs4 import BeautifulSoup

# with open('index6.html', 'r') as file:
#     soup = BeautifulSoup(file.read(), 'html.parser')
    
#     for i in soup.find_all('body'):
#         if i.find('div', attrs={'class':'container'}):
#             if i.find('h1') and i.find('h1').get_text() == "Google Play Terms of Service":
#                 print("성공")                
#         else:
#             print("실패")

# #components of container - 3

# from bs4 import BeautifulSoup

# with open('index6.html', 'r') as file:
#     soup = BeautifulSoup(file.read(), 'html.parser')
    
#     for i in soup.find_all('body'):
#         if i.find('div', attrs={'class':'container'}):
#             if i.find('h6') and i.find('h6').get_text() == "February 5, 2018":
#                 print("성공")                
#         else:
#             print("실패")

# #components of container - 4

# from bs4 import BeautifulSoup

# with open('index6.html', 'r') as file:
#     soup = BeautifulSoup(file.read(), 'html.parser')
    
#     for i in soup.find_all('body'):
#         if i.find('div', attrs={'class':'container'}):
#             if i.find('h2') and i.find('h2').get_text() == "1. Introduction":
#                 print("성공")                
#         else:
#             print("실패")

# #components of container - 5

# from bs4 import BeautifulSoup

# with open('index6.html', 'r') as file:
#     soup = BeautifulSoup(file.read(), 'html.parser')
    
#     for i in soup.find_all('body'):
#         if i.find('div', attrs={'class':'container'}):
#             if i.find('p') and i.find('p').get_text() == '''Applicable Terms. Thanks for using Google Play. Google Play is a service provided by Google LLC ("Google", "we" or "us"), located at 1600 Amphitheatre Parkway, Mountain View, California 94043, USA. Your use of Google Play and the apps (including Android Instant Apps), games, music, movies, books, magazines, or other digital content or services (referred to as "Content") available through it is subject to these Google Play Terms of Service and the Google Terms of Service ("Google ToS") ( together referred to as the "Terms"). Google Play is a "Service" as described in the Google ToS. If there is any conflict between the Google Play Terms of Service and the Google ToS, the Google Play Terms of Service shall prevail.''':
#                 print("성공")                
#         else:
#             print("실패")

#components of container - 6

from bs4 import BeautifulSoup

with open('index6.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    
    for i in soup.find_all('body'):
        if i.find('div', attrs={'class':'container'}):
            if i.find('h2') and i.find('h2').get_text() == "2. Your Use of Google Play": #첫 번째 h2의 태그가 출력되어 에러 발생. -> 같은 태그가 두 개 이상 나왔을 경우 문제
                print("성공")
            else: 
                print("실패")                
        else:
            print("실패")
