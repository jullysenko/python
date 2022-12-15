from view import input_data as in_d

data = in_d()
print(data)
def import_txt(dt):
    with open('text.txt', 'a', encoding='utf-8') as file_data:
        for i in range(len(dt)):
            file_data.writelines(f'{dt[i]}'+';')

import_txt(data)