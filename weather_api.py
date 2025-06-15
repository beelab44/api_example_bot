import requests

def get_weather(city: str) -> str:
    """
    Отримує інформацію про погоду з публічного API для заданого міста.
    
    Аргументи:
        city (str): Назва міста англійською (наприклад, 'Kyiv').
    
    Повертає:
        str: Текстовий опис поточної погоди та прогнозу на 3 дні.
    """
    # Формуємо URL для запиту до API
    url = f"https://goweather.xyz/weather/{city}"
    
    try:
        # Відправляємо GET-запит до API
        response = requests.get(url)
        
        # Перевіряємо статус-код відповіді
        if response.status_code != 200:
            return f"Помилка: не вдалося отримати дані про погоду. Код відповіді: {response.status_code}"
        
        # Перетворюємо JSON-відповідь у словник
        data = response.json()
        
        # Витягуємо основні поля
        temp = data.get("temperature", "Невідомо")
        wind = data.get("wind", "Невідомо")
        desc = data.get("description", "Немає опису")
        
        # Формуємо текст повідомлення про поточну погоду
        result = f"Погода у місті {city}:\n"
        result += f"Температура: {temp}\n"
        result += f"Вітер: {wind}\n"
        result += f"Опис: {desc}\n\n"
        
        # Додаємо прогноз на наступні 3 дні (якщо є)
        forecast = data.get("forecast", [])
        if forecast:
            result += "Прогноз на 3 дні:\n"
            for day in forecast:
                day_num = day.get("day", "?")
                day_temp = day.get("temperature", "?")
                day_wind = day.get("wind", "?")
                result += f"День {day_num}: Температура {day_temp}, Вітер {day_wind}\n"
        
        return result

    except requests.RequestException as e:
        # Обробка помилок під час запиту
        return f"Помилка з'єднання: {e}"


def get_random_duck():
    url = "https://random-d.uk/api/v2/random"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("url")
    else:
        return None
        




