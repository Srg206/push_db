import csv

def normalize_company_names(csv_file):

  with open(csv_file, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)  # Получаем заголовок

    # Находим индекс столбца 'client_company'
    company_index = header.index('client_company')

    # Создаем новый файл для записи измененных данных
    with open("refactored"+csv_file, 'w', newline='') as outfile:
      writer = csv.writer(outfile)
      writer.writerow(header)  # Записываем заголовок

      # Проходим по каждой строке CSV-файла
      for row in reader:
        # Меняем значения в столбце 'client_company'
        row[company_index] = row[company_index].replace('Д2', 'd2').replace('Лизинг', 'leasing').replace('Экспобанк', 'expobank')
        row[company_index] = row[company_index].replace('Хвоя', 'hvoya').replace('Автоэкспресс', 'autoexpress').replace('Expocar', 'expocar')
        writer.writerow(row)

# Замените 'your_file.csv' на имя вашего CSV-файла
normalize_company_names('hackaton_client_data.csv')
