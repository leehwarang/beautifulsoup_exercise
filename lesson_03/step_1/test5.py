from bs4 import BeautifulSoup

with open('index5.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    try:
        pre_tag = soup.body.find('ul', class_="information")
        tag = pre_tag.find_all('li')
    except AttributeError:
        assert()
    assert(
        len(tag) == 3
        and tag[0].text.strip() == 'Orc' and tag[0].get('class')[0] == 'job'
        and tag[1].text.strip() == '+1.23.456.7890' and tag[1].get('class')[0] == 'phone'
        and tag[2].text.strip() == 'jonathan@blackrockclan.com' and tag[2].get('class')[0] == 'mail'
    )



'''
In the `<ul>`, add `<li>` and apply the following classes to each of the information: job position/phone number/email. 
<ul class="information">
    <li class="job">Orc</li>
    <li class="phone">+1.23.456.7890</li>
    <li class="mail">jonathan@blackrockclan.com</li>
  </ul>
'''

# from bs4 import BeautifulSoup

# with open('index5.html', 'r') as file:
#     soup = BeautifulSoup(file.read(), 'html.parser')

#     for i in soup.find_all('body'):
#         if i.find_all('div', attrs={'class':'business-card'}):
#             if i.find('ul', attrs={'class':'information'}):
#                 if i.find('li', attrs={'class':'job'}) and i.find('li', attrs={'class':'phone'}) and i.find('li', attrs={'class':'mail'}):
#                     print("성공")
#                 else: 
#                     print("실패")
                    # li_list = i.find_all('li')
                    # b = i.find_all('li', attrs={'class':'job'})
                    # a = li_list[0]
                    # if i.find_all('li', attrs={'class':'job'}):
                    #     print("성공")
                    #     print(a)
                    #     print(b)
                    # else: 
                    #     print("실패")
                    #     print(a)
                    #     print(b)
                    # #if li_list[0].get_text()) == "Orc" and
                    # #print(li_list[0].className())