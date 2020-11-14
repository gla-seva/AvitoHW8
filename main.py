import json
from advert import Advert

if __name__ == '__main__':
    # создаем экземпляр класса Advert из JSON
    lesson_str = """{
        "title": "python",
        "price": 0,
        "location": {
            "address": "город Москва, Лесная, 7", 
            "metro_stations": ["Белорусская"]
            }
        }"""
    lesson = json.loads(lesson_str)

    lesson_ad = Advert(lesson)
    # обращаемся к атрибуту location.address
    print(lesson_ad.location.address, flush=True)

    lesson_str = '{"title": "python"}'
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad.price)

    print(lesson_ad)
