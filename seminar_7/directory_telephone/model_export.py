def export_txt():
    with open('text.txt', 'r', encoding='utf-8') as data:
        string_data = data.readlines()
        print(string_data)

export_txt()