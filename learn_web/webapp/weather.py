import requests
import configparser

config = configparser.ConfigParser()
config.read("config.ini")


def weather_by_city(city_name):
    weather_url = config['LEARNWEB']['weather_url']
    params = {
        "key": config['LEARNWEB']['weather_url_key'],
        "q": city_name,
        "format": "json",
        "num_of_days": 1,
        "lang": "ru"
    }
    try:
        result = requests.get(weather_url, params=params)
        weather = result.json()
        if "data" in weather:
            if "current_condition" in weather["data"]:
                try:
                    return weather["data"]["current_condition"][0]
                except(IndexError, TypeError):
                    return False
    except (requests.RequestException, ValueError):
        print("Сетевая ошибка ")
        return False
    return False


if __name__ == "__main__":
    w = weather_by_city("Moscow, Russia")
    print(w)
