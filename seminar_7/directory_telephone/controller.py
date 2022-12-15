import view
import model_import
import model_export


def button_click():
    cho = view.choise()
    if cho == '1':
        model_import.import_txt()
    elif cho== '2':
        data = model_export.export_txt()
        print(data)

