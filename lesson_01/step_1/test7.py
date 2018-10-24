from bs4 import BeautifulSoup

with open('index7.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    first_tag = soup.body.find_all('h2')
    second_tag = soup.body.find_all('p')

    assert(
        len(first_tag) == 2
        and len(second_tag) == 2 #p태그는 내용이 길어서 text 검사 안함
        and first_tag[1].text.strip() == '2. Your Use of Google Play'
        and first_tag[1].previous_sibling.previous_sibling.name == 'p'
        and second_tag[1].previous_sibling.previous_sibling.name == 'h2'
        and first_tag[1].find_parent('div')
        and second_tag[1].find_parent('div')
    )

# from bs4 import BeautifulSoup

# with open('index6.html', 'r') as file:
#     soup = BeautifulSoup(file.read(), 'html.parser')
#     h2_list = []
#     for i in soup.find_all('body'):
#         if i.find('div', attrs={'class':'container'}):
#             h2_list = i.find_all('h2')
#     assert(h2_list[1].get_text() == "2. Your Use of Google Play")

# from bs4 import BeautifulSoup

# with open('index6.html', 'r') as file:
#     soup = BeautifulSoup(file.read(), 'html.parser')
#     p_list = []
#     for i in soup.find_all('body'):
#         if i.find('div', attrs={'class':'container'}):
#             p_list = i.find_all('p')
#     assert(p_list[1].get_text() == """Access to and Use of Content. You may use Google Play to browse, locate, view, stream, or download Content for your mobile, computer, tv, watch, or other supported device ("Device"). To use Google Play, you will need a Device that meets the system and compatibility requirements for the relevant Content, working Internet access, and compatible software. The availability of Content and features will vary between countries and not all Content or features may be available in your country. Some Content may be available to share with family members. Content may be offered by Google or made available by third-parties not affiliated with Google. Google is not responsible for and does not endorse any Content made available through Google Play that originates from a source other than Google.""")