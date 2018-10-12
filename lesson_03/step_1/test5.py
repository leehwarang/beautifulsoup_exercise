'''
In the `<ul>`, add `<li>` and apply the following classes to each of the information: job position/phone number/email. 
<ul class="information">
    <li class="job">Orc</li>
    <li class="phone">+1.23.456.7890</li>
    <li class="mail">jonathan@blackrockclan.com</li>
  </ul>
'''

from bs4 import BeautifulSoup

with open('index5.html', 'r') as file:
    soup = BeautifulSoup(file.read(), 'html.parser')

    for i in soup.find_all('body'):
        if i.find_all('div', attrs={'class':'business-card'}):
            if i.find('ul', attrs={'class':'information'}):
                if i.find_all('li'):
                    li_list = i.find_all('li')
                    #if li_list[0].get_text()) == "Orc" and
                    print(li_list[0].className())