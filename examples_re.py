import re

text1 = 'Thi1s i22s si3mple te4xt for examples in regular expressions'

print('\n----------------------------')
find = re.search('\d', text1)  # \d any one digits (in our case its '1')
print(find)  # object match
print('True' if find else 'No')
print(find[0])  # first in find
print(find.start())  # position that find
print(re.split('\d', text1))  # split text by expression

print('\n----------------------------')
find = re.search('\d{2}', text1)  # \d any one digits * 2 (in our case its '22')
print(find)  # object match
print('True' if find else 'No')
print(find[0])  # first in find
print(find.start())  # position that find

print('\n----------------------------')
find = re.search('ex.mple', text1)  # . any symbol except \n (in our case ' "a" in example')
print(find)  # object match
print('True' if find else 'No')
print(find[0])  # first in find
print(find.start())  # position that find

