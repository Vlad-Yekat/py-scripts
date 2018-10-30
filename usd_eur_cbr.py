'''
we think that cbr contains
<tr>
      <td>840</td>
      <td>USD</td>
      <td>1</td>
      <td>Доллар США</td>
      <td>65,7742</td>
    </tr>
or same
'''
from bs4 import BeautifulSoup
import requests

def get_course():
    url = "https://www.cbr.ru/currency_base/daily/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    course_str = requests.get(url)

    soup = BeautifulSoup(course_str.text, 'html.parser')
    nessesary_cur = ['USD', 'EUR']

    course_dict = []
    for arr in soup.find_all("td"):
        course_dict.append(arr.text)

    for arr in range(len(course_dict)):
        if course_dict[arr] in nessesary_cur:
            cur = str(course_dict[arr+2]) +': '+ str(course_dict[arr+3])
            print(cur)


get_course()