'''
Написать регулярное выражение, которое будет проверять формат времени. (14:00 - True, 25:66 - False)
'''

import re


pattern = r"([0-1][0-9]|[2][0-3]):[0-5][0-9]"
match = re.fullmatch(pattern, input("Введите время в формате '__:__': "))
if match:
    print(True)
else:
    print(False)
