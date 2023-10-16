import openpyxl

# Открываем Excel-файл
workbook = openpyxl.load_workbook('example.xlsx')

# Выбираем лист с данными
sheet = workbook['Лист1']  # Замените 'Лист1' на имя вашего листа

# Функция для поиска фамилии по имени
def find(name):
    for row in sheet.iter_rows(min_row=2, values_only=True):
        if row[0] == name:
            return row[1]
    return "вопрос не найден"

# Пример использования
