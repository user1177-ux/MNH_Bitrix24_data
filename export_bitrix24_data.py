import requests
import csv

# Настройки
webhook_url = 'https://b24-ll5zno.bitrix24.ru/rest/16/2ew5qznxbyfuzk6l/crm.deal.list.json'
params = {
    'filter[>DATE_CREATE]': '2024-07-01T00:00:00Z',
    'filter[<DATE_CREATE]': '2024-07-15T23:59:59Z',
    'filter[STAGE_ID]': '2',  # ID воронки сделок
    'select[]': 'ID',
    'select[]': 'DATE_CREATE',
    'select[]': 'STAGE_ID',
    'select[]': 'TITLE'
}

response = requests.get(webhook_url, params=params)
deals = response.json().get('result', [])

# Сохранение данных в CSV
with open('deals_data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['ID', 'DATE_CREATE', 'STAGE_ID', 'TITLE'])
    for deal in deals:
        writer.writerow([deal['ID'], deal['DATE_CREATE'], deal['STAGE_ID'], deal['TITLE']])

print("Данные успешно выгружены и сохранены в файл deals_data.csv")
