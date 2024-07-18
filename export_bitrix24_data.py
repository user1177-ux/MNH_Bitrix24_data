import requests
import csv
from datetime import datetime

def fetch_data():
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

    print("Отправка запроса к API...")
    response = requests.get(webhook_url, params=params)
    print("Ответ от API получен.")

    if response.status_code != 200:
        print(f"Ошибка при запросе данных: {response.status_code}")
        print(response.text)
        return

    deals = response.json().get('result', [])
    print(f"Найдено сделок: {len(deals)}")

    if not deals:
        print("Нет данных для указанного периода.")
        return

    file_path = 'deals_data.csv'
    print("Запись данных в файл...")
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'DATE_CREATE', 'STAGE_ID', 'TITLE'])
        for deal in deals:
            writer.writerow([deal['ID'], deal['DATE_CREATE'], deal['STAGE_ID'], deal['TITLE']])

    with open(file_path, 'a') as f:
        f.write(f"\n# Last updated: {datetime.now().isoformat()}\n")

    print("Данные успешно выгружены и сохранены в файл", file_path)
    print("Содержимое файла после записи данных:")
    with open(file_path, 'r', encoding='utf-8') as f:
        print(f.read())

if __name__ == "__main__":
    fetch_data()
