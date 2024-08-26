import time
from time import sleep
from datetime import timedelta
from threading import Thread


def write_words(word_count, file_name):
    start_time = time.time()
    with open(file_name, 'w', encoding='utf-8') as file:
        for word in range(1, word_count + 1):
            file.write(f"Какое-то слово № {word}" + '\n')
            sleep(0.1)
    end_time = time.time()
    print(f"Завершилась запись в файл {file_name}. Время выполнения: {round(end_time - start_time, 2)} сек")


data_base = [
    (10, 'example1.txt'),
    (30, 'example2.txt'),
    (200, 'example3.txt'),
    (100, 'example4.txt')]

global_start = time.time()

launchs = [write_words(word_count=words, file_name=names) for words, names in data_base]

global_end = time.time()
global_result = timedelta(seconds=global_end - global_start)
print(f'Время записи всех файлов составило: {global_result}')

stream_start = time.time()

streams = [Thread(target=write_words, args=task) for task in data_base]

for stream in streams:
    stream.start()

for stream in streams:
    stream.join()

stream_end = time.time()
stream_time = timedelta(seconds=stream_end - stream_start)
print(f'Время потоковой записи всех файлов составило: {stream_time}')
