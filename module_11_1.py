import json
import requests
import pandas as pd
import matplotlib.pyplot as plt
from threading import Thread
from multiprocessing import Pool

API_KEY = '61018d48297e4161b35384014bf610aa'
URL = 'https://api.rawg.io/api/games'


class Download(Thread):  # Собираем комбайн для сборки урожая!
    def __init__(self, params, page, URL):
        super().__init__()
        self.params = params
        self.URL = URL
        self.page = page

    def run(self):
        params_with_page = self.params.copy()  # Каждому комбайну - свой мануальчик!
        params_with_page['page'] = self.page  # Каждому комбайну - своё поле. Навигация!
        try:
            response = requests.get(self.URL, params=params_with_page)  # Основной модуль работы комбайна
            self.result = response.json()  # Рядом едет грузовик, туда сгружаем пшеницу!
        except requests.exceptions.RequestException as e:  # Проверяем, не отвалилось ли чего :D
            self.result = None
            print(f"Произошла ошибка при запросе данных {e}")


threads = []  # Амбарчики
all_results = []  # Гига-Амбар

for page in range(1, 6):  # 5 полей пшеницы насчитывают наши владения на сегодняшний день(этого достаточно)
    params = {'key': API_KEY, 'ordering': '-metacritic', 'page_size': 100}  # Возьмем только самую отборную!
    thread = Download(params=params, page=page, URL=URL)  # К работе готовы!
    thread.start()  # Пуск!
    threads.append(thread)  # Собираем урожай!

for thread in threads:
    thread.join()  # Принимаем отчет о завершении работ

for thread in threads:
    if thread.result:  # А вдруг отлынивал?
        all_results.extend(
            thread.result.get('results', []))  # Доставляем урожай со всех полей в наш здоровенный амбар :D

with open('games_data.json', 'w', encoding='utf-8') as file:  # Наш трудовой подвиг будет увековечен в архивах!
    json.dump(all_results, file, indent=4, ensure_ascii=False)


#################  Конец первой части  #################


def transform_data(game):  # Хорошо поработали комбайны. Собрали вообще всё! И землю, и камни, и брёвна и пшеницу... :D
    info_to_get = ['name', 'genres', 'released', 'rating']  # Нам бы просто пшеницу...
    return {
        info: game.get(info, None) for info in info_to_get  # Настроим наше супер-сито! Собирает только зёрна!
    } | {'genres': [genre['name'] for genre in game.get('genres', [])]}  # Часть сырья вся в грязи, надо отмыть!
# На всех зёрнышках есть особая наномаркировка, но из-за дождя, у некоторых она смылась. Не взять их - большая ОШИБКА!

def process_data(games):  # Супер-сито! Работает в 4 руки! Или что там у него...
    with Pool(processes=4) as pool:
        processed_data = pool.map(transform_data, games)  # Особый механизм. Распределитель-объединитель(результата)
    return processed_data


def load_data(file_path):  # Открывай архив! Посмотрим на фронт наших работ.
    with open(file_path, 'r', encoding='utf-8') as file:
        data_open = json.load(file)
    return data_open


def save_to_csv(data, output_file):  # Тамара Васильевна Панда. Наш бухгалтер.
    df = pd.DataFrame(data)  # Её отчеты всегда образцово выглядят!
    df_sorted = df.sort_values(by='rating', ascending=False)  # Я попросил её начать запись с самых отборных зёрен.
    df_sorted.to_csv(output_file, index=False, encoding='utf-8')  # С таким отчётом, хоть к президенту!


if __name__ == "__main__":  # Супер-сито работает только в присутствии главного инженера! Таков закон.
    games = load_data('games_data.json')  # Загружаем нашу "кучу всего"
    processed_data = process_data(games)  # Супер-сито к пуску готово!
    save_to_csv(processed_data, 'games_data.csv')  # Наша Панда - круче всех!
                                                            # С ней нас ждёт большой успех!
#################  Конец второй части  #################

    pandata = pd.read_csv('games_data.csv')  # По случаю юбилея нашего предприятия, я попросил Тамару Васильевну...
    pandata['released'] = pd.to_datetime(pandata['released'], errors='coerce')  # Проанализировать и собрать важные даты...
    pandata['release_year'] = pandata['released'].dt.year  # Года, наших трудовых подвигов!
    games_per_year = pandata['release_year'].value_counts().sort_index()  # Я покажу вам историю, проверенную временем!


    def plot_games_per_year(data):  # Мы назовём её: "Шкала вдохновения"
        plt.figure(figsize=(12, 6))
        plt.plot(games_per_year.index, games_per_year.values, marker='o')
        plt.xlabel('Год выпуска')
        plt.ylabel('Количество игр')
        plt.title('Шкала вдохновения')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.show()

    plot_games_per_year(games_per_year) # Финальный аккорд!

#################  Конец   #################
# Послесловие
# Возвращаясь с полей к видеоиграм. Мне захотелось показать на графике именно эти данные, так как...
# Так как они наглядно демонстрируют время подъема и спада творческой мысли игровой индустрии.
# Скачивая данные с параметром -метакритик, я старался взять игры с самыми высокими оценками.
# И хотя, ты, уважаемый читатель, мог не встретить в этом списке свою любимую игру, а иную, мог видеть впервые...
# Данная выборка демонстрирует общий, если так можно сказать, выбор человечества....
# А ты уже можешь для себя решить сам, пришелся ли он тебе по душе.
# Тебе я желаю всего самого наилучшего!
# Спасибо и удачи!
