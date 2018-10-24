from bs4 import BeautifulSoup

with open('index2.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    tag = soup.body.find('div', class_="container").find_next('img', src="https://res.cloudinary.com/dyiqg9qhi/image/upload/v1538867822/img_google_play_f0vk76.png")

    assert(
        tag
        and tag.find_parent('div')
    )

#첫 번째 test code
# from bs4 import BeautifulSoup

# with open('index2.html', 'r') as file:
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

# with open('index2.html', 'r') as file:
#     answer_dict = [{'name':'img', 'src':'https://res.cloudinary.com/dyiqg9qhi/image/upload/v1538867822/img_google_play_f0vk76.png'}]

#     soup = BeautifulSoup(file.read(), 'html.parser')
#     soup = soup.body.div

#     for i in soup.contents:
#         if i == '\n':
#             soup.contents.remove(i)
    
#     for answer in answer_dict:
#         for content in soup.contents:
#             if answer['name'] == content.name and answer['src'] == content['src']:
#                 print("성공")
#             else:
#                 print("실패")
    
    #print(answer_dict[0]['name']) 
    #print(soup.contents[0].name) # 태그들이 전부 리스트에 들어감.
    #print(answer_dict[0]['src'])
    #print(soup.contents[0]['src'])


# #=========이전 코드
# from bs4 import BeautifulSoup

# with open('index.html', 'r') as file:
#     soup = BeautifulSoup(file.read(), 'html.parser')
    
#     for i in soup.find_all('body'):
#         assert(i.find_all('div', attrs={'class':'container'}) and i.find('img', attrs={'src':'https://res.cloudinary.com/dyiqg9qhi/image/upload/v1538867822/img_google_play_f0vk76.png', 'alt':"Google Play"}))

# #개선할 점
# #body에서 div가 있는지 찾았다면, div에 img가 있는지 찾을 때는 div에서만 검사하면 되는거 아닌가? -> TC를 2개 만드는 방식

# #TC1: body에서 div가 1개 있는지 검사
# #TC2: div에서 img가 1개 있는지 검사

# #이렇게 만들었을 때의 장점은? 중첩 if문과 and 연산자를 안써도 됨. 검색할 때 계속 큰 body를 기준으로 검색하는게 아니라 점점 좁혀가면서 검색할 수 있음.
