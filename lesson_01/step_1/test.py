from bs4 import BeautifulSoup

with open('index.html', 'r') as file:
    answer_dict = [{'name':'div', 'class':'container'}]

    soup = BeautifulSoup(file.read(), 'html.parser')
    soup = soup.body
    for i in soup.contents:
        if i == '\n':
            soup.contents.remove(i)
    #print(soup.contents) # 태그들이 전부 리스트에 들어감. 
    for answer in answer_dict:
        for content in soup.contents:
            if answer['name'] == content.name and answer['class'] == content['class'][0]:
                print("성공")
            else: 
                print("실패")

    # print(soup.contents[0])
    # print(soup.contents[0].name) #태그의 이름 구하기
    # print(soup.contents[0]['class'][0]) #태그의 클래스 구하기

    #정답 리스트(딕셔너리 형태)만들어 놓고, 정답이랑 soup.contents에 들어가 있는 애랑 같다면 정답으로 처리할 수 있음.
    








    # 이전 코드
    # for i in soup.find('body'):
    #     assert(i.find_all('div', attrs={'class':'container'})) #참이면 아무 것도 하지않고, 거짓이면 오류 메세지 출력

#개선할 점
#index.html에는 body 태그와 div 태그가 하나여야함.- > find_all로 하되, 찾은 태그의 개수가 1개씩인지 체크해야함.