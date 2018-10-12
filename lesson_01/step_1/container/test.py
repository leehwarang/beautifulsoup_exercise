# #components of container
# from bs4 import BeautifulSoup

# with open('index.html', 'r') as file:
#     soup = BeautifulSoup(file.read(), 'html.parser')
    
#     for i in soup.find('body'):
#         if i.find('div', attrs={'class':'container'}):
#             print("성공")
#         else:
#             print("실패")





# from bs4 import BeautifulSoup

# with open('index.html', 'r') as file:
#     soup = BeautifulSoup(file.read(), 'html.parser')

#     # Use at least one assertion
#     assert(len(soup.find_all('div')) == 1)


from bs4 import BeautifulSoup

with open('index.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    
    for i in soup.find_all('body'):
        assert(i.find_all('div', attrs={'class':'container'})) #참이면 아무 것도 하지않고, 거짓이면 오류 메세지 출력

#개선할 점
#index.html에는 body 태그와 div 태그가 하나여야함.- > find_all로 하되, 찾은 태그의 개수가 1개씩인지 체크해야함.
