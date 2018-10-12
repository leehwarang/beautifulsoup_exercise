# #components of container - 1

# from bs4 import BeautifulSoup

# with open('index2.html', 'r') as file:
#     soup = BeautifulSoup(file.read(), 'html.parser')
    
#     for i in soup.find_all('body'):
#         if i.find('div', attrs={'class':'container'}):
#             assert(i.find('h1') and i.find('h1').get_text() == "Google Play Terms of Service")


from bs4 import BeautifulSoup

with open('index2.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    
    for i in soup.find_all('body'):
        if i.find('div', attrs={'class':'container'}):
            assert(i.find('h1') and i.find('h1').get_text() == "Google Play Terms of Service")

#개선 할 점
#TC를 3개로 나누어야 함. 
#TC1: body에 div가 1개 있는지
#TC2: div에 img가 1개 있는지
#TC3: div에 img 밑에 h1이 1개 있는지 -> 하위에 있다는걸 어떻게 검수하지? -> div 하위에 들어가는 태그들을 리스트에 넣어서,
#리스트의 원소 개수를 세고 인덱스로 뒤에 위치해있는지 비교해야 하나?