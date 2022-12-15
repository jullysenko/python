import view

data = view.input_data()
print(data)
def import_txt():
    global data
    with open('text.txt', 'a', encoding='utf-8') as file_data:
        for i in range(len(data)):
            file_data.writelines(f'{data[i]}'+';')

import_txt()