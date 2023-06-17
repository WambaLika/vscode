import requests

def search_cheapest_tickets(origin, destination, date):
    api_key = 'YOUR_API_KEY'  # Вставьте ваш API-ключ для доступа к соответствующему сервису бронирования билетов

    # Формируем URL-запрос с использованием параметров поиска
    url = f'https://api.example.com/tickets?origin={origin}&destination={destination}&date={date}&api_key={api_key}'

    try:
        response = requests.get(url)
        data = response.json()

        if 'error' in data:
            print(f"Ошибка при получении данных: {data['error']}")
            return

        tickets = data['tickets']

        if len(tickets) == 0:
            print("Билеты не найдены.")
        else:
            cheapest_ticket = min(tickets, key=lambda ticket: ticket['price'])
            print(f"Самый дешевый билет: {cheapest_ticket['airline']} - {cheapest_ticket['price']} {cheapest_ticket['currency']}")
        
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при отправке запроса: {str(e)}")

# Пример использования
origin = 'CityA'
destination = 'CityB'
date = '2023-07-01'

search_cheapest_tickets(origin, destination, date)
