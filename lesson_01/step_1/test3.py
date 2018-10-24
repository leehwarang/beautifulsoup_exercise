from bs4 import BeautifulSoup

with open('index3.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    tag = soup.body.find('img', src="https://res.cloudinary.com/dyiqg9qhi/image/upload/v1538867822/img_google_play_f0vk76.png").find_next('h1')
    
    assert(
        tag
        and tag.text.strip() =='Google Play Terms of Service'
        and tag.find_parent('div')
    )

#첫 번째 test code
# from bs4 import BeautifulSoup

# with open('index3.html', 'r') as file:
#     answer_dict = [{'name':'div', 'class':'container'}]

#     soup = BeautifulSoup(file.read(), 'html.parser')
#     soup = soup.body
#     for i in soup.contents:
#         if i == '\n':
#             soup.contents.remove(i)
#     #print(soup.contents) # 태그들이 전부 리스트에 들어감. 
#     for answer in answer_dict:
#         for content in soup.contents:
#             if answer['name'] == content.name and answer['class'] == content['class'][0]:
#                 print("성공")
#             else: 
#                 print("실패")


#두 번째 test code
# from bs4 import BeautifulSoup

# with open('index3.html', 'r') as file:
#     answer_dict = [{'name':'img', 'src':'https://res.cloudinary.com/dyiqg9qhi/image/upload/v1538867822/img_google_play_f0vk76.png'},
#                     {'name':'h1'}]

#     print(answer_dict)

#     soup = BeautifulSoup(file.read(), 'html.parser')
#     soup = soup.body.div

#     for i in soup.contents:
#         if i == '\n':
#             soup.contents.remove(i)
    
#     print(soup.contents)
#     for answer, j in enumerate(answer_dict):
#         for content in soup.contents:
#             if j == 0:
#                 if answer['name'] == content.name and answer['src'] == content['src']:
#                     print("성공")
#                 else:
#                     print("실패")
#                     break
#             elif j == 1:
                
#             else:
#                 print("실패")








# #=====================이전 코드
# from bs4 import BeautifulSoup

# with open('index2.html', 'r') as file:
#     soup = BeautifulSoup(file.read(), 'html.parser')
    
#     for i in soup.find_all('body'):
#         if i.find('div', attrs={'class':'container'}):
#             assert(i.find('h1') and i.find('h1').get_text() == "Google Play Terms of Service")

# #개선 할 점
# #TC를 3개로 나누어야 함. 
# #TC1: body에 div가 1개 있는지
# #TC2: div에 img가 1개 있는지
# #TC3: div에 img 밑에 h1이 1개 있는지 -> 하위에 있다는걸 어떻게 검수하지? -> div 하위에 들어가는 태그들을 리스트에 넣어서,
# #리스트의 원소 개수를 세고 인덱스로 뒤에 위치해있는지 비교해야 하나?