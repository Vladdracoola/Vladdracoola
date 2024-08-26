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


global_start = time.time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

global_end = time.time()
global_result = timedelta(seconds=global_end - global_start)
print(f'Время записи всех файлов составило: {global_result}')

stream_start = time.time()

stream_1 = Thread(target=write_words, args=(10, 'example5.txt'))
stream_2 = Thread(target=write_words, args=(30, 'example6.txt'))
stream_3 = Thread(target=write_words, args=(200, 'example7.txt'))
stream_4 = Thread(target=write_words, args=(100, 'example8.txt'))

stream_1.start()
stream_2.start()
stream_3.start()
stream_4.start()

stream_1.join()
stream_2.join()
stream_3.join()
stream_4.join()

stream_end = time.time()
stream_time = timedelta(seconds=stream_end - stream_start)
print(f'Время потоковой записи всех файлов составило: {stream_time}')
